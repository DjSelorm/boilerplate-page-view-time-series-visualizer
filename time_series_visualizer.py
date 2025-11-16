# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('/content/fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# Clean data
# Keep only data within the 2.5th and 97.5th percentile
lower = df['value'].quantile(0.025)
upper = df['value'].quantile(0.975)
df = df[(df['value'] >= lower) & (df['value'] <= upper)]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(df.index, df['value'], color='red', linewidth=1)

    # Set title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Improve x-axis ticks for readability
    plt.xticks(rotation=45)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    #plt.close(fig) # Close the figure to prevent repeated display
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Draw bar plot

    # Group by year and month, then calculate mean
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Create the figure
    fig = df_grouped.plot(kind='bar', figsize=(14, 8), legend=True).figure

    # Customize plot
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    #plt.close(fig) # Close the figure to prevent repeated display
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))

    # Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0], palette='viridis')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box Plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1],
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],legend=False, palette='plasma')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')


   
    #plt.close(fig) # Close the figure to prevent repeated display
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
