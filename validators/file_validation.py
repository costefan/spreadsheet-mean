import functools
import pandas as pd


class FileValidator:
    """File validation and mutation rules.
    """

    REQUIRED_COLUMNS = ('Date', 'Visitors',)

    def __init__(self, df):
        self.df = df

    def _validate_file_structure(self):
        if set(self.REQUIRED_COLUMNS) - set(self.df.columns):
            raise Exception('There is not all required columns in file')

    def _convert(self, col_name: str):
        if col_name == 'Date':
            convert_func = functools.partial(pd.to_datetime, errors='coerce')
        else:
            convert_func = functools.partial(pd.to_numeric, errors='coerce')

        self.df[col_name] = self.df[col_name].apply(convert_func)
        self.df = self.df[~pd.isnull(self.df[col_name])]

    def _validate_date(self):
        self._convert(col_name='Date')
        # implementing other validation logic

    def _validate_visitors(self):
        self._convert(col_name='Visitors')

    def __call__(self, *args, **kwargs):
        self._validate_file_structure()
        self._validate_date()
        self._validate_visitors()

        return self.df
