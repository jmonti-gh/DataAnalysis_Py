import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
#print(df.head())
# print(df)
# cont = input('Press enter to continue...')

# Add 'overweight' column
df['overweight'] = [1 if x > 25 else 0 for x in df.weight / ((df.height * 0.01) ** 2)]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1,
# make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df.cholesterol.map(lambda x: 0 if x == 1 else 1)
df['gluc'] = df.gluc.map(lambda x: 0 if x == 1 else 1)
# print(df)
# cont = input('Press enter to continue...')

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc',
    # 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars='cardio',
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # print('df_cat:\n', df_cat.sample(5))
    # cont = input('Press enter to continue...')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    # You will have to rename one of the columns for the catplot to work correctly.
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio','variable', 'value'], as_index=False).count()
    # print('df_cat-G:\n', df_cat.sample(5))
    # cont = input('Press enter to continue...')
    
    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(data= df_cat, x='variable', y= 'total', col='cardio', hue='value', kind='bar')
    # print('type(g:', type(g))

    # Get the figure for the output
    fig = g.figure
    # print('type(fig):', type(fig))

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():

    # Clean the data                                        # Filter Out:
    df_heat = df.loc[
        (df['ap_lo'] <= df['ap_hi']) &                      # diastolic p. > systolic p.
        (df['height'] >= df['height'].quantile(0.025)) &    # height < 2.5th percentile
        (df['height'] <= df['height'].quantile(0.975)) &    # height > 97.5th percentile
        (df['weight'] >= df['weight'].quantile(0.025)) &    # weight < 2.5th percentile
        (df['weight'] <= df['weight'].quantile(0.975))      # weight > 97.5th percentile
    ]
    # print('df_heat\n', df_heat)
    # cont = input('Press enter to continue...')

    # # Calculate the correlation matrix
    corr = df_heat.corr()

    # # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))
    #fig, ax = plt.subplots()

    # # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, linewidths= .5,
                     center= 0.00, vmin= -0.16, vmax= 0.32, square=True,
                     cbar_kws={'shrink': .5, 'ticks': [-.08, .0, .08, .16, .24]})

    # # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

def dhm1():
    # Clean the data
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize= (12, 10))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, vmax=.3, center=0,
                square=True, linewidths=.5,
                cbar_kws={"shrink": .5, 'ticks': [-.08, .0, .08, .16, .24] })

    # Do not modify the next two lines
    fig.savefig('heatm1.png')
    return fig

#print(draw_cat_plot())
draw_heat_map()
dhm1()