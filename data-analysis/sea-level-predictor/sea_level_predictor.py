import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], alpha=0.5, s=1, color="blue")

    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = range(1880, 2051)
    plt.plot(x, res.intercept + res.slope * x, color="orange", linewidth=1)

    # Create second line of best fit
    res = linregress(
        df.loc[df["Year"] >= 2000, "Year"], df.loc[df["Year"] >= 2000, "CSIRO Adjusted Sea Level"]
    )
    x = range(2000, 2051)
    plt.plot(x, res.intercept + res.slope * x, color="red", linewidth=1)

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    """
    * The x label should be "Year", the y label should be "Sea Level (inches)", and the title should be "Rise in Sea Level".
    """
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
