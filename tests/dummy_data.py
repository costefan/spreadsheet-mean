import pandas as pd


TEST_DATAFRAME_1 = pd.DataFrame(
    {'Date': ['10.02.2015', '10.02.2015', '17.02.2015', '18.02.2015'],
     'Visitors': [10, 20, 30, 10]}
)

TEST_DATAFRAME_FAILED = pd.DataFrame(
    {'Date': ['10.02.2015', '10.02.2015', '17.02.2015', '18.02.2015'],
     'Visibors': [10, 20, 30, 10]}
)

TEST_DATAFRAME_2 = pd.DataFrame(
    {'Date': ['10.02.015', '10.02.2015', '17.02.2015', '18.02.2015'],
     'Visitors': [10, 20, 30, 10]}
)