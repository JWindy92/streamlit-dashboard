import json
import os
from pathlib import Path

import pandas as pd

DEFAULT_DATA_PATH = Path("sample_data/balances.json")

CONFIG_PATH = Path("config/financial_accounts.json")


def load_display_accounts(
    path: str | Path = CONFIG_PATH,
) -> list[str]:
    """Load account IDs selected for dashboard display."""
    with Path(path).open("r", encoding="utf-8") as file:
        config = json.load(file)

    accounts = config.get("display_accounts")

    if not isinstance(accounts, list) or not all(
        isinstance(account, str) for account in accounts
    ):
        raise ValueError("display_accounts must be a list of account IDs.")

    return accounts


def load_balances(path: str | Path | None = None) -> pd.DataFrame:
    """Load persisted financial account balances from a JSON file."""
    data_path = Path(
        path
        or os.getenv(
            "FINANCIAL_DATA_PATH",
            DEFAULT_DATA_PATH,
        )
    )

    if not data_path.exists():
        raise FileNotFoundError(f"Financial data file not found: {data_path}")

    with data_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Expected a JSON array of account balances.")

    df = pd.DataFrame(data)
    required = {"id", "name", "balance", "currency"}

    if not required.issubset(df.columns):
        raise ValueError(f"Missing required columns: {required - set(df.columns)}")

    df["balance"] = pd.to_numeric(df["balance"], errors="raise")

    return df
