import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
#print(df.head())
print(df)
cont = input('Press enter to continue...')

# Add 'overweight' column
df['overweight'] = [1 if x > 25 else 0 for x in df.weight / ((df.height * 0.01) ** 2)]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1,
# make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df.cholesterol.map(lambda x: 0 if x == 1 else 1)
df['gluc'] = df.gluc.map(lambda x: 0 if x == 1 else 1)
print(df)
cont = input('Press enter to continue...')

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc',
    # 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars='cardio',
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    print('df_cat:\n', df_cat.sample(5))
    cont = input('Press enter to continue...')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    # You will have to rename one of the columns for the catplot to work correctly.
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio','variable', 'value'], as_index=False).count()
    print('df_cat-G:\n', df_cat.sample(5))
    cont = input('Press enter to continue...')
    
    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(data= df_cat, x='variable', y= 'total', col='cardio', hue='value', kind='bar')
    print('type(g:', type(g))

    # Get the figure for the output
    fig = g.figure
    print('type(fig):', type(fig))

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

print(draw_cat_plot())
