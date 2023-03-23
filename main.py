from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
# # to view graphs in notebook
# %matplotlib inline
import plotly
import cufflinks as cf
# # For offline use
# cf.go_offline()

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

# find max close price for each bank's stock
bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()

# create a dataframe with the returns for each bank's stock
returns = pd.DataFrame()

for tick in tickers:
    returns[tick + ' Return'] = bank_stocks[tick]['Close'].pct_change()
 
# create a pairplot of the returns dataframe using seaborn
sns.pairplot(returns)

# find dates each bank stock had the best and worst single day returns
returns.idxmax()
returns.idxmin()

# find standard deviation of the returns over the entire period and for specific year
returns.std()
returns.loc['2015-01-01':'2015-12-31'].std()

# create a histogram of returns achieved in specfic year and stock using seaborn
sns.histplot(returns.loc['2015-01-01':'2015-12-31']['MS Return'],color='green',bins=100)
sns.histplot(returns.loc['2008-01-01':'2008-12-31']['C Return'],color='red',bins=100)

# create an interactive line plot using cufflinks showing close price for each bank stock
bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()

# create a heatmap of the correlation between the stocks Close Price
sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)

# create a candle plot of Bank of America's stock from Jan 1st 2015 to Jan 1st 2016
BAC[['Open', 'High', 'Low', 'Close']].loc['2015-01-01':'2016-01-01'].iplot(kind='candle')

# create a Simple Moving Averages plot of Morgan Stanley for the year 2015
MS['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study='sma',periods=[13,21,55],title='Simple Moving Averages')

# create a Bollinger Band Plot for Bank of America for the year 2015
BAC['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study='boll')
