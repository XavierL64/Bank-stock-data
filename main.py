from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
# # to view graphs in notebook
# %matplotlib inline

# # extract stock data from 2006 to 2016 using Remote Data Access
start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)
# Bank of America
BAC = data.DataReader("BAC", 'stooq', start, end)
# CitiGroup
C = data.DataReader("C", 'stooq', start, end)
# Goldman Sachs
GS = data.DataReader("GS", 'stooq', start, end)
# JPMorgan Chase
JPM = data.DataReader("JPM", 'stooq', start, end)
# Morgan Stanley
MS = data.DataReader("MS", 'stooq', start, end)
# Wells Fargo
WFC = data.DataReader("WFC", 'stooq', start, end)

# creata dataframe using concatenation
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC],axis=1,keys=tickers)

# set column name levels
bank_stocks.columns.names = ['Bank Ticker','Stock Info']
