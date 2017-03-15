"""
I don`t use unittests framework, pytest is more pythonic
"""

import pandas as pd
import pytest

from validators.file_validation import FileValidator
from .dummy_data import (
    TEST_DATAFRAME_1, TEST_DATAFRAME_FAILED, TEST_DATAFRAME_2,
)


def test_result_type():
    validator = FileValidator(TEST_DATAFRAME_1)
    df = validator()

    assert isinstance(df, pd.DataFrame)


def test_not_all_cols():
    with pytest.raises(Exception):
        validator = FileValidator(TEST_DATAFRAME_FAILED)
        validator()


def test_rows_result_count():
    validator = FileValidator(TEST_DATAFRAME_2)
    df = validator()

    assert df.shape[0] == 3
