Backtest trading Strategies using various technical indicators

#Install The library 
pip install QuantPanda

#DataFrame Struture 
date | open | high | low | close | volume

#Snippet of a Simple Moving Average Crossover

from quantpanda import QuantPanda
import pandas as pd

#dataframe
df = pd.read_csv(r'INFY.csv')

#generate tradelog for a Simple Moving Average Crossover of 100
QuantPanda.SimpleMovingAverageCrossover(df, 100)

#List of technical indicators:
1.  Simple Moving Crossover
2.  Exponential Moving Crossover
3.  Double Crossover Simple Moving Crossover
4.  Double Crossover Exponential Moving Crossover
5.  RSI
6.  Adx
7.  Supertrend
8.  William's R Indicator
9.  Parabolic SAR
10. MACD
11. Bollinger Bands
12. Donchian Channels
13. Heikin Ashi
