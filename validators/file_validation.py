import functools
import pandas as pd


class FileValidator:
    """File validation and mutation rules.
    """

    REQUIRED_COLUMNS = ('Date', 'Visitors',)

    def __init__(self, data):
        self.data = data
        self.df = None

    def _validate_file_structure(self):

        if set(self.REQUIRED_COLUMNS) - set(self.data.get('values')[0]):
            raise Exception('There is not all required columns in file')

    def _prepare_dataframe(self):
        indexes_reqired_cols = [
            self.data.get('values')[0].index(col)
            for col in self.REQUIRED_COLUMNS
        ]
        print(indexes_reqired_cols)
        # deleting column names from obj
        self.data.get('values').pop(0)
        print(self.data.get('values'))
        values = []
        for ind, _ in enumerate(self.data.get('values')):
            values.append([])
            for index in indexes_reqired_cols:
                try:
                    values[ind].append(_[index])
                except IndexError:
                    values[ind].append('0')

        self.df = pd.DataFrame(
            values, columns=self.REQUIRED_COLUMNS
        )

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
        self._prepare_dataframe()
        self._validate_date()
        self._validate_visitors()

        return self.df
