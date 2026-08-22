import pandas as pd

from src.saving import save_data


def test_save_data(tmp_path):
    df = pd.DataFrame({
        "id": [1, 2],
        "name": ["Ali", "Sara"]
    })

    file_path = tmp_path / "output.csv"

    save_data(
        df,
        file_path
    )

    assert file_path.exists()

    loaded = pd.read_csv(file_path)

    assert len(loaded) == 2
    assert list(loaded.columns) == ["id", "name"]