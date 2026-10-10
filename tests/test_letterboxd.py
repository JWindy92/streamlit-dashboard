import json

from data.letterboxd import load_activity


def test_load_activity(tmp_path):
    path = tmp_path / "activity.json"
    path.write_text(
        json.dumps([{"title": "Test Film", "rating": 4.0}]),
        encoding="utf-8",
    )

    df = load_activity(path)

    assert len(df) == 1
    assert df.iloc[0]["title"] == "Test Film"
    assert df.iloc[0]["rating"] == 4.0
