import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

# Clean data
df = df.loc[
    (df["value"].quantile(0.025) <= df["value"]) & (df["value"] <= df["value"].quantile(0.975))
]

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    fig.set_size_inches(32.0, 10.0)
    fig.set_dpi(100)
    df_line = df.copy()
    df_line["value"].plot(
        ax=ax,
        xlabel="Date",
        ylabel="Page Views",
        title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
        ylim=(0, None),
        color="red",
    )

    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().groupby(by=[df.index.month, df.index.year]).mean()
    df_bar.index.names = ["month", "year"]
    df_bar.sort_values(by=["year", "month"], inplace=True)
    df_bar.reset_index(level=0, inplace=True)
    df_bar = df_bar.pivot(columns="month", values="value")

    df_bar.rename(columns=months, inplace=True)

    # Draw bar plot
    fig, ax = plt.subplots()
    fig.set_size_inches(15.14 / 2, 13.30 / 2)
    fig.set_dpi(100 * 2)
    df_bar.plot(
        ax=ax,
        xlabel="Years",
        ylabel="Average Page Views",
        kind="bar",
    )
    ax.legend(title="Months")

    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(32.0, 11.2)
    fig.set_dpi(100)

    plot_year = sns.boxplot(x="year", y="value", data=df_box, ax=axs[0])
    plot_year.set(xlabel="Year", ylabel="Page Views")
    plot_year.set_title("Year-wise Box Plot (Trend)")
    # ax[0].legend(title="Months")
    plot_month = sns.boxplot(
        x="month",
        y="value",
        data=df_box,
        ax=axs[1],
        order=[s[:3] for s in months.values()],
    )
    plot_month.set(xlabel="Month", ylabel="Page Views")
    plot_month.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig
