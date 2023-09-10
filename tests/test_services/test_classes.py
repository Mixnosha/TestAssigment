from typing import Any, Tuple
from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from testassigment.services import read_from_csv_file
from testassigment.services.classes import PlotManager
from tests.test_services import TIMESTAMP_PRICE_DATA, PRICE_DATA

DF_WITH_EMA = [
        # {span} = 10
        [
            1875.979748793,
            1876.3931285054603,
            1876.9309985287182,
            1877.6059704598467,
            1877.9290358217295,
            1877.6178997963375,
            1877.7050908687095,
            1878.1660741926355,
            1878.7241418258086,
            1879.618058305045,
            1880.662639518873,
            1881.675315790154
            ]
        ]

OHLC_OPEN_PRICE = [
        # {time_period: '5Min'}
        [1875.979748793, 1876.7313482702, 1877.979748793, 1885.7311357534]
        ]

OHLC_HIGH_PRICE = [
        # {time_period: '5Min'}
        [1875.979748793, 1878.979748793, 1884.7313482702, 1885.7311357534]
        ]

OHLC_LOW_PRICE = [
        # {time_period: '5Min'}
        [1875.979748793, 1876.7311357534, 1877.979748793, 1885.7311357534]
        ]

OHLC_CLOSE_PRICE = [
        # {time_period: '5Min'}
        [1875.979748793, 1876.7311357534, 1884.7313482702, 1885.7311357534]
        ]



class TestPlotManager:

    @staticmethod
    @pytest.fixture(scope="function")
    @patch(
            "builtins.open",
            new_callable=mock_open,
            read_data=TIMESTAMP_PRICE_DATA
            )
    def df(_) -> pd.DataFrame:
        return PlotManager.create_df_from_csv_file("file_path")


    @staticmethod
    @patch(
            "builtins.open",
            new_callable=mock_open,
            read_data=TIMESTAMP_PRICE_DATA
            )
    def test_create_df_from_csv_file(_) -> None:
        df = read_from_csv_file("file_path")
        price_list = df["Price"].tolist()
        assert price_list == PRICE_DATA

    @staticmethod
    @patch(
            "builtins.open",
            new_callable=mock_open,
            read_data="""
            error file
            12313, 1312321, 123123, 213213,
            """
            )
    def test_error_create_df_from_csv_file(_) -> None:
        with pytest.raises(pd.errors.ParserError):
            read_from_csv_file("file_path")


    @staticmethod
    @pytest.mark.parametrize(
            "params", [
                # time period, index in the correct data
                ("5Min", 0)
                ]
            )
    def test_format_ohlc(params: Tuple[str, int], df: pd.DataFrame) -> None:
        time_period, index = params
        ohlc_df = PlotManager.format_ohlc(
                df=df,
                time_period=time_period
                )
        assert ohlc_df["open"].tolist() == OHLC_OPEN_PRICE[index]
        assert ohlc_df["high"].tolist() == OHLC_HIGH_PRICE[index]
        assert ohlc_df["low"].tolist() == OHLC_LOW_PRICE[index]
        assert ohlc_df["close"].tolist() == OHLC_CLOSE_PRICE[index]

    @staticmethod
    @pytest.mark.parametrize(
            "params", [
                # time_period, error
                ("5", ValueError),
                ("aaa", ValueError),
                ("5aaa", ValueError),
                ]
            )
    def test_error_time_period_format_ohlc(
            params: Tuple[str, Any],
            df: pd.DataFrame
            ) -> None:
        time_period, error = params
        with pytest.raises(error):
            PlotManager.format_ohlc(
                df=df,
                time_period=time_period
            )

    @staticmethod
    @pytest.mark.parametrize(
            "params", [
                # span, index in the correct data
                (10, 0)
                ]
            )
    def test_add_ema(params: Tuple[int, int], df: pd.DataFrame) -> None:
        span, index = params
        df_with_ema = PlotManager.add_ema(
                df=df,
                span=span
                )
        assert df_with_ema["ema"].to_list() == DF_WITH_EMA[index]


