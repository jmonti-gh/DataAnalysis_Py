import pandas as pd

#!head data/sales_data.csv

sales = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])
#print(sales.head())
print(sales.shape)
#print(sales.info())
#print(sales.describe())
print(sales['Unit_Cost'].mean())

import matplotlib.pyplot as plt
import matplotlib_inline

#%matplotlib inline

print(sales['Unit_Cost'].plot())
print(sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6)))