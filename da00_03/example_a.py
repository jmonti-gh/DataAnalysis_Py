import pandas as pd
import matplotlib.pyplot as plt

#!head data/sales_data.csv - # bash-shell command 'head'

sales = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])
#print(sales.head())    # .head(n=5), first 5 rows of DF w/cos titles
#print(sales.tail())    # .tail(n=5), last 5 rows of DF w/cos titles
#print(sales)            # print all de DF as a table (using ... for large data)
print(sales.shape)      # (rows, cols) tuple
#print(sales.info())    # DF structure info
#print(sales.describe())    # DF cols statistics values
print(sales['Unit_Cost'].mean())    # mean of Unic_Cost column

sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))     # box plot Unit_Cost col
plt.show()          # necesary to display the graph