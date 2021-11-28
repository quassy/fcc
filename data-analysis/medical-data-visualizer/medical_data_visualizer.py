import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
# df["bmi"] = df["weight"] / (df["height"] / 100) ** 2
df.loc[df["weight"] / (df["height"] / 100) ** 2 <= 25, "overweight"] = 0
df.loc[df["weight"] / (df["height"] / 100) ** 2 > 25, "overweight"] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc'
# is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1
df.loc[df["gluc"] == 1, "gluc"] = 0
df.loc[df["gluc"] > 1, "gluc"] = 1


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol',
    # 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(
        df,
        id_vars=["id", "cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You
    # will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(by=["cardio", "variable", "value"], as_index=False).count()

    # Draw the catplot with 'sns.catplot()'
    fig, ax = plt.subplots()
    sns.catplot(
        x="variable",
        y="id",
        hue="value",
        kind="bar",
        col="cardio",
        data=df_cat,
    )

    # Do not modify the next two lines
    fig.savefig("catplot.png")
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[df["ap_lo"] <= df["ap_hi"]]
    df_heat = df_heat.loc[df_heat["height"].quantile(0.025) <= df_heat["height"]].loc[
        df_heat["height"] <= df_heat["height"].quantile(0.975)
    ]

    df_heat = df_heat.loc[df_heat["weight"].quantile(0.025) <= df_heat["weight"]].loc[
        df_heat["weight"] <= df_heat["weight"].quantile(0.975)
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones(corr.shape))

    # Set up the matplotlib figure
    fig, ax = plt.subplots()
    fig.set_size_inches(11.0, 9.0)
    fig.set_dpi(100)

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt=".1f", mask=mask, linewidths=0.5)

    # Do not modify the next two lines
    fig.savefig("heatmap.png")
    return fig
