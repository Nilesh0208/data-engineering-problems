from __future__ import annotations
import pandas as pd
from pathlib import Path
from .config import CLEAN_OUTPUT_FILE, QUARANTINE_FILE
from .quality_rules import find_quality_issues, VALID_STATUSES
from .audit_logger import AuditLogger


CRITICAL_SEVERITY = "critical"
DATE_COLUMNS = ["order_date", "updated_at"]


def _normalize_record(record: dict[str, str]) -> dict[str, str]:
    normalized = {}
    for key, value in record.items():
        if value is None or pd.isna(value):
            normalized[key] = ""
        elif isinstance(value, str):
            normalized[key] = value.strip()
        elif hasattr(value, "strftime"):
            try:
                if hasattr(value, "hour"):
                    normalized[key] = value.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    normalized[key] = value.strftime("%Y-%m-%d")
            except (ValueError, TypeError):
                normalized[key] = ""
        else:
            normalized[key] = value

    if normalized.get("order_status"):
        normalized["order_status"] = normalized["order_status"].upper()
    return normalized


def _is_critical_issue(issues: list[dict[str, str]]) -> bool:
    return any(issue["severity"] == CRITICAL_SEVERITY for issue in issues)


def _parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    for col in DATE_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


class RemediationAgent:
    def __init__(self, audit_logger: AuditLogger):
        self.audit_logger = audit_logger

    def remediate(self, raw_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        raw_df = raw_df.copy()
        raw_df = _parse_dates(raw_df)
        seen_order_ids: set[str] = set()
        clean_rows = []
        quarantine_rows = []

        for record in raw_df.to_dict(orient="records"):
            normalized = _normalize_record(record)
            issues = find_quality_issues(normalized, seen_order_ids)
            order_id = normalized.get("order_id", "")
            has_critical = _is_critical_issue(issues)

            if has_critical:
                quarantine_rows.append(normalized)
                for issue in issues:
                    self.audit_logger.log(order_id, issue["rule"], "quarantined", "Critical issue detected")
                continue

            if any(issue["rule"] == "duplicate_order_id" for issue in issues):
                self.audit_logger.log(order_id, "duplicate_order_id", "deduplicated", "Keeping latest record by updated_at")

            clean_rows.append(normalized)
            for issue in issues:
                if issue["severity"] != CRITICAL_SEVERITY:
                    self.audit_logger.log(order_id, issue["rule"], "reviewed", "Non-critical issue recorded")

            if order_id:
                seen_order_ids.add(order_id)

        output_df = pd.DataFrame(clean_rows)
        quarantine_df = pd.DataFrame(quarantine_rows)
        output_df = self._deduplicate(output_df)
        self._write_output(output_df, CLEAN_OUTPUT_FILE)
        self._write_output(quarantine_df, QUARANTINE_FILE)
        return output_df, quarantine_df

    def _deduplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        if df.empty or "order_id" not in df.columns:
            return df
        if "updated_at" not in df.columns:
            return df.drop_duplicates(subset=["order_id"], keep="last")
        sorted_df = df.sort_values(by=["order_id", "updated_at"], ascending=[True, False])
        return sorted_df.drop_duplicates(subset=["order_id"], keep="first")

    def _write_output(self, df: pd.DataFrame, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)
