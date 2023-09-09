import pandas as pd


def read_from_csv_file(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(
            file_path,
            skiprows=1,
            header=None,
            names=["Timestamp", "Price"],
            index_col=0,
            parse_dates=["Timestamp"]
            )
    return df

