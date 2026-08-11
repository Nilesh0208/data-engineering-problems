import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
PARENT_DIR = ROOT_DIR

if str(PARENT_DIR) not in sys.path:
    sys.path.insert(0, str(PARENT_DIR))
