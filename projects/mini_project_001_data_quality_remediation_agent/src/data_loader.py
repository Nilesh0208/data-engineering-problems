import pandas as pd
from .config import INPUT_FILE


def load_raw_orders() -> pd.DataFrame:
    return pd.read_csv(INPUT_FILE, dtype=str, keep_default_na=False)
