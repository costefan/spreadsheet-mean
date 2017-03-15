from calc import Calculator
import pandas as pd
from .dummy_data import TEST_DATAFRAME_1


def test_result_type():
    mean_df = Calculator.rolling_mean(
        data=TEST_DATAFRAME_1, by='Visitors', grouper_col='Date')

    assert isinstance(mean_df, pd.DataFrame)


def test_result_cols():
    mean_df = Calculator.rolling_mean(
        data=TEST_DATAFRAME_1, by='Visitors', grouper_col='Date')

    assert len(mean_df.columns.values) == 3
    assert sorted(list(mean_df.columns.values)) == [
        'Date', 'Moving Average', 'Visitors', ]


def test_result_cols_values():
    mean_df = Calculator.rolling_mean(
        data=TEST_DATAFRAME_1, by='Visitors', grouper_col='Date')

    assert list(mean_df['Moving Average'].values) == [0, 0, 30, 20]
