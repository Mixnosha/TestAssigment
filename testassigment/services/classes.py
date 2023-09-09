import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
from services.reader import read_from_csv_file


class PlotManager:

    """
    brief: Simple manager for working with valuable data.
    """

    @staticmethod
    def create_df_from_csv_file(file_path: str) -> pd.DataFrame:

        """
        brief: method creates a pandas dataframe based on the csv file.
        parms:
            file_path: types:str; full path to the file.csv
        requirements:
            file_format: {Timestamp}, {Price}.

        """

        return read_from_csv_file(file_path)


    @staticmethod
    def format_ohlc(df: pd.DataFrame, time_period: str) -> pd.DataFrame:

        """
        brief: method returns a dataframe in ohlc format.
        params:
            df: Pandas:DataFrame; in the form {Timestamp}, {Price}.
            time_period: types:str; time in pandas standart.
        """

        try:
            return df["Price"].resample(time_period, closed="right").ohlc().ffill()
        except ValueError as e:
            print(e)
            exit()

    @staticmethod
    def add_ema(df: pd.DataFrame, span: float) -> pd.DataFrame:

        """
        brief: standard pandas function for finding computers EMA.
            a = 2 / (span + 1), for span >= 1
        """

        try:
            return df.assign(
                ema=df["Price"].ewm(
                    span=span,
                    ).mean()
                )
        except ValueError as e:
            print(e)
            exit()


class Draw:

    """
    brief: class for displaying graphs based on a Pandas:DataDrame.
    """

    @staticmethod
    def draw_plot_from_df(df: pd.DataFrame) -> None:
        df.plot()
        plt.title("Plot")
        plt.show()

    @staticmethod
    def draw_candles_plot_from_df(df: pd.DataFrame) -> None:
        mpf.plot(df, type='candle', style='yahoo', title='Candle Plot', ylabel='Price')
