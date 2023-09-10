import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd

from testassigment.services.reader import read_from_csv_file


class PlotManager:

    """
    brief: Simple manager for working with valuable data.
    """

    @staticmethod
    def create_df_from_csv_file(file_path: str) -> pd.DataFrame:

        """
        brief: method creates a pandas dataframe based on the csv file.
        parms:
            {file_path}: [types:str] full path to the file.csv
        requirements:
            file_format: {Timestamp}, {Price}.

        """

        return read_from_csv_file(file_path)


    @staticmethod
    def format_ohlc(df: pd.DataFrame, time_period: str) -> pd.DataFrame:
        """
        Compute open, high, low and close values of a group, excluding missing values.

        For multiple groupings, the result index will be a MultiIndex

        Parameters
        ----------

        time_period: string
            Must be in a pandas compatible format.

        Returns
        -------
        DataFrame
            Open, high, low and close values within each group.
        """

        return df["Price"].resample(time_period, closed="right").ohlc().ffill()

    @staticmethod
    def add_ema(df: pd.DataFrame, span: float) -> pd.DataFrame:

        r"""
        Parameters
        ----------

        span : float, optional
            Specify decay in terms of span

            :math:`\alpha = 2 / (span + 1)`, for :math:`span \geq 1`.
        """

        return df.assign(
                ema=df["Price"].ewm(
                    span=span,
                    ).mean()
                )


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
