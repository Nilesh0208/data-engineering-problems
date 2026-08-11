from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_DIR = BASE_DIR / "data" / "input"
OUTPUT_DIR = BASE_DIR / "data" / "output"
QUARANTINE_DIR = BASE_DIR / "data" / "quarantine"
INPUT_FILE = INPUT_DIR / "raw_orders.csv"
CLEAN_OUTPUT_FILE = OUTPUT_DIR / "clean_orders.csv"
QUARANTINE_FILE = QUARANTINE_DIR / "quarantined_orders.csv"
AUDIT_LOG_FILE = OUTPUT_DIR / "audit_log.csv"
