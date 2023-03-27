import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x_ori = df['Year']
    y_ori = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, axe = plt.subplots(figsize=(12, 8))
    axe.scatter(x= x_ori, y= y_ori, label='Original data')
    axe.grid(color='gray', linestyle='--', linewidth= .5)

    # Create first line of best fit
    gain, intercept, rvalue, pvalue, sterr = linregress(x_ori, y_ori)
    x_rest = pd.Series([i for i in range(2014, 2051)])
    x_all = pd.concat([x_ori, x_rest])
    y_pred_all = intercept + gain * x_all

    axe.plot(x_all, y_pred_all, color='green', label='Line of best fit from 1880')

    # Create second line of best fit
    df_2k = df.loc[df['Year'] >= 2000]          # subset only from year 2k
    df_2k.reset_index(inplace=True)             # Not necessary at all
    x_2k = df_2k['Year']
    y_2k = df_2k['CSIRO Adjusted Sea Level']
    gain2k, intercept2k, rvalue2k, pvalue2k, sterr2k = linregress(x_2k, y_2k)
    x_2k_2k50 = pd.concat([x_2k, x_rest])
    y_pred_2k = intercept2k + gain2k * x_2k_2k50

    axe.plot(x_2k_2k50, y_pred_2k, color='red', label='Line of best fit from 2000')

    # Add labels and title
    axe.set_title('Rise in Sea Level')
    axe.set_xlabel('Year')
    axe.set_ylabel('Sea Level (inches)')
    axe.legend(loc='upper left')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
plt.show()
