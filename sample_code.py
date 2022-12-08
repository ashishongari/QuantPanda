from quantpanda import QuantPanda
import pandas as pd

#read the data frame | format of data | date | open | high | low | close | volume
df = pd.read_csv(r'INFY.csv')

#generate tradelog of Simple Moving Average Crossover of 100 
print(QuantPanda.SimpleMovingAverageCrossover(df, 100))
