import pandas as pd


class Calculator:

    @classmethod
    def rolling_mean(cls, data, by: str='Visitors',
                     grouper_col: str='Date') -> pd.DataFrame:
        """
        Calculating rolling mean
        :param data: dataframe
        :param by: what column calculate
        :param grouper_col: by what column group
        :return:
        """
        moving_avg = data.sort_values(
            by=grouper_col)\
            .groupby(grouper_col)[by].sum()\
            .rolling(2).mean()\
            .fillna(0)

        return data.merge(
            moving_avg.to_frame(name='Moving Average').reset_index(),
            on=grouper_col
        )
