import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Create first line of best fit (from 1880 to 2050)
    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    line1 = slope1 * years_extended + intercept1
    plt.plot(years_extended, line1, color='red', label='Best Fit Line (1880-2050)')

    # Create second line of best fit (from 2000 to 2050)
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    line2 = slope2 * years_recent + intercept2
    plt.plot(years_recent, line2, color='green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
