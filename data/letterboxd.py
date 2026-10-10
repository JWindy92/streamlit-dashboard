import json
import os
from pathlib import Path

import pandas as pd

DEFAULT_DATA_PATH = Path("sample_data/activity.json")


def load_activity(path: str | Path | None = None) -> pd.DataFrame:
    """Load persisted Letterboxd activity from a JSON file."""
    data_path = Path(path or os.getenv("LETTERBOXD_DATA_PATH", DEFAULT_DATA_PATH))

    if not data_path.exists():
        raise FileNotFoundError(f"Letterboxd data file not found: {data_path}")

    with data_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict):
        data = data.get("activity", data.get("entries", [data]))

    if not isinstance(data, list):
        raise ValueError(
            "Expected a JSON array or an object containing activity/entries."
        )

    return pd.DataFrame(data)
