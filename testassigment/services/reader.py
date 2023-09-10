import pandas as pd


def read_from_csv_file(file_path: str) -> pd.DataFrame:
    """
    brief: The function creates a pandas dataframe based on the ssv file.
    params: {file_path} [types:str], full path to the file.csv.

    warn: The function discards the first line in the file.
          Only '{Timestamp},{Price}' format.
    """
    return pd.read_csv(
            file_path,
            skiprows=1,
            header=None,
            names=["Timestamp", "Price"],
            index_col=0,
            parse_dates=["Timestamp"]
            )


