from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from testassigment.services import read_from_csv_file
from tests.test_services import PRICE_DATA, TIMESTAMP_PRICE_DATA


class TestReader:


    @staticmethod
    @patch(
            "builtins.open",
            new_callable=mock_open,
            read_data=TIMESTAMP_PRICE_DATA
            )
    def test_read_from_csv_file(_):
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
    def test_error_read_from_csv_file(_):
        with pytest.raises(pd.errors.ParserError):
            read_from_csv_file("file_path")

