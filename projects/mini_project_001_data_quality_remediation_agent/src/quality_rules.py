from datetime import datetime
from typing import Dict, List, Any


VALID_STATUSES = {"NEW", "PROCESSING", "COMPLETED", "CANCELLED"}


def rule_missing_order_id(record: Dict[str, Any]) -> bool:
    return not bool(record.get("order_id", "").strip())


def rule_missing_customer_id(record: Dict[str, Any]) -> bool:
    return not bool(record.get("customer_id", "").strip())


def rule_negative_order_amount(record: Dict[str, Any]) -> bool:
    amount = record.get("order_amount", "").strip()
    try:
        return float(amount) < 0
    except ValueError:
        return True


def rule_invalid_order_status(record: Dict[str, Any]) -> bool:
    status = record.get("order_status", "").strip().upper()
    return status not in VALID_STATUSES


def rule_invalid_order_date(record: Dict[str, Any]) -> bool:
    raw_date = record.get("order_date", "")
    if raw_date is None:
        return True
    date_text = raw_date.strip() if isinstance(raw_date, str) else str(raw_date)
    if not date_text:
        return True
    try:
        order_date = datetime.strptime(date_text[:10], "%Y-%m-%d")
        return order_date.date() > datetime.utcnow().date()
    except ValueError:
        return True


def find_quality_issues(record: Dict[str, Any], seen_order_ids: set) -> List[Dict[str, str]]:
    issues = []
    if rule_missing_order_id(record):
        issues.append({"rule": "missing_order_id", "severity": "critical"})
    if rule_missing_customer_id(record):
        issues.append({"rule": "missing_customer_id", "severity": "critical"})
    if rule_negative_order_amount(record):
        issues.append({"rule": "negative_order_amount", "severity": "critical"})
    if rule_invalid_order_status(record):
        issues.append({"rule": "invalid_order_status", "severity": "warning"})
    if rule_invalid_order_date(record):
        issues.append({"rule": "invalid_order_date", "severity": "warning"})
    if record.get("order_id") and record["order_id"] in seen_order_ids:
        issues.append({"rule": "duplicate_order_id", "severity": "warning"})
    return issues
