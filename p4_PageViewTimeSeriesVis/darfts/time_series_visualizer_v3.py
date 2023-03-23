import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar as cal

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df.loc[(df['value'] > df['value'].quantile(0.025)) &
            (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize= (15, 5), dpi=200)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.plot(df, color='firebrick')
    fig.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year 
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    df_bar.rename(columns=lambda c: cal.month_name[c], inplace=True)

    # Draw bar plot
    fig, axe = plt.subplots(figsize= (8, 7), dpi=200)
    df_bar.plot(kind='bar', ax=axe)
    axe.set_xlabel('Years')
    axe.set_ylabel('Average Page Views')
    axe.legend(title='Months')

    # https://blakeaw.github.io/2020-05-25-improve-matplotlib-notebook-inline-res/
    # https://www.scaler.com/topics/matplotlib/matplotlib-control-the-output-resolution/
    # https://stackoverflow.com/questions/47633546/relationship-between-dpi-and-figure-size
    # https://www.tutorialspoint.com/how-do-you-improve-matplotlib-image-quality

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    #fig, axes = plt.subplots(1, 2, figsize=(16, 6), dpi=150)     # 1 row, 2 charts in this row
    fig, axes = plt.subplots(1, 2, figsize=(40, 15), dpi=70)     # 1 row, 2 charts in this row
    ylabel = 'Pate Views'
    yticks = [i * 20_000 for i in range(11)]
    titfsize = 30
    axsfsize = titfsize/1.3

    # 1st chart: distributed values within a given year. Tit: Year-wise Box Plot (Trend)
    sns.boxplot(x=df_box.year, y=df_box.value, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)', fontsize=titfsize)
    axes[0].set_ylabel(ylabel, fontsize=axsfsize)
    axes[0].set_xlabel('Year', fontsize=axsfsize)
    axes[0].set_yticks(yticks)
    axes[0].tick_params(axis='both', labelsize=axsfsize)

    # 2nd chart: distributed values within a given month. Tit: Month-wise Box Plot (Seasonality)
    months = [cal.month_abbr[i] for i in range (1, 13)]
    sns.boxplot(x=df_box.month, y=df_box.value, ax=axes[1], order=months)
    axes[1].set_title('Month-wise Box Plot (Seasonality)', fontsize=titfsize)
    axes[1].set_ylabel(ylabel, fontsize=axsfsize)
    axes[1].set_xlabel('Month', fontsize=axsfsize)
    axes[1].set_yticks(yticks)
    axes[1].tick_params(axis='both', labelsize=axsfsize)

    fig.tight_layout(pad=titfsize/4)

# https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
# https://www.geeksforgeeks.org/change-font-size-in-matplotlib/
# https://pythonguides.com/matplotlib-tick-params/
# https://www.geeksforgeeks.org/how-to-set-tick-labels-font-size-in-matplotlib/
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html
# https://www.tutorialspoint.com/how-to-change-xticks-font-size-in-a-matplotlib-plot


    ### --- FUTURE DO all of fontsize & labelsize & maybe other with...
    # Set the font dictionaries (for plot title and axis titles)
    """ title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'normal',
                'verticalalignment':'bottom'} # Bottom vertical alignment for more space
    axis_font = {'fontname':'Arial', 'size':'14'}

    # Set the font properties (for use in legend)   
    font_path = 'C:\Windows\Fonts\Arial.ttf'
    font_prop = font_manager.FontProperties(fname=font_path, size=14)

    ax = plt.subplot() # Defines ax variable by creating an empty plot

    # Set the tick labels font
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontname('Arial')
        label.set_fontsize(13)

    x = np.linspace(0, 10)
    y = x + np.random.normal(x) # Just simulates some data

    plt.plot(x, y, 'b+', label='Data points')
    plt.xlabel("x axis", **axis_font)
    plt.ylabel("y axis", **axis_font)
    plt.title("Misc graph", **title_font)
    plt.legend(loc='lower right', prop=font_prop, numpoints=1)
    plt.text(0, 0, "Misc text", **title_font)
    plt.show() """

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_line_plot()
draw_bar_plot()
draw_box_plot()
#plt.show()
