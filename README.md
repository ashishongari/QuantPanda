Backtest trading strategies using various technical indicators
______________________________________________________________

#Install The library 

pip install QuantPanda

#DataFrame Struture : date | open | high | low | close | volume

______________________________________________________________
Snippet of a Simple Moving Average Crossover
______________________________________________________________

from quantpanda import QuantPanda

import pandas as pd

df = pd.read_csv(r'INFY.csv')


#Final output will be tradelog. Format of tradelog : Entry Date | Entry Price | Exit Date | Exit Price

tradelog_df = QuantPanda.SimpleMovingAverageCrossover(df, 100)


#Generate Performance Metrics

QuantPanda.PerformanceMetrics(tradelog_df)

______________________________________________________________

List of technical indicators:
1.  Simple Moving Crossover
2.  Exponential Moving Crossover
3.  Double Crossover Simple Moving Crossover
4.  Double Crossover Exponential Moving Crossover
5.  RSI
6.  ADX
7.  Supertrend
8.  William's R Indicator
9.  Parabolic SAR
10. MACD
11. Bollinger Bands
12. Donchian Channels
13. Heikin Ashi
