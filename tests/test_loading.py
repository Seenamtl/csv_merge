import pandas as pd

from src.loading import load_data


def test_load_existing_csv(tmp_path):
    file_path = tmp_path / "test.csv"

    df = pd.DataFrame({
        "id": [1, 2],
        "name": ["Ali", "Sara"]
    })

    df.to_csv(file_path, index=False)

    result = load_data(file_path)

    assert result is not None
    assert len(result) == 2
    assert list(result.columns) == ["id", "name"]


def test_load_missing_csv(tmp_path):
    file_path = tmp_path / "missing.csv"

    result = load_data(file_path)

    assert result is None