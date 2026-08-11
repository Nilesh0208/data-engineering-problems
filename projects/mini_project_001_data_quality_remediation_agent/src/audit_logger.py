import csv
from datetime import datetime
from pathlib import Path
from .config import AUDIT_LOG_FILE


AUDIT_FIELDS = ["timestamp", "order_id", "rule", "action", "reason"]


class AuditLogger:
    def __init__(self):
        self._path = AUDIT_LOG_FILE
        self._ensure_directory()
        self._write_header()

    def _ensure_directory(self):
        self._path.parent.mkdir(parents=True, exist_ok=True)

    def _write_header(self):
        if not self._path.exists():
            with open(self._path, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=AUDIT_FIELDS)
                writer.writeheader()

    def log(self, order_id: str, rule: str, action: str, reason: str) -> None:
        with open(self._path, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=AUDIT_FIELDS)
            writer.writerow({
                "timestamp": datetime.utcnow().isoformat(),
                "order_id": order_id,
                "rule": rule,
                "action": action,
                "reason": reason,
            })
