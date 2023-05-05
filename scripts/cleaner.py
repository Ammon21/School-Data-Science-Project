#Cleaner Scripts
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class cleaner:

    def percent_missing(df: pd.DataFrame):
        # Calculate total  number of cells in dataframe
        totalCells = np.product(df.shape)

        # Count number of missing values per column
        missingCount = df.isnull().sum()

        # Calculate total number of missing values
        totalMissing = missingCount.sum()

        # Calculate percentage of missing values
        return print("The dataset contains", round(((totalMissing / totalCells) * 100), 2), "%", "missing values.")

    def plot_outlier(df,columns,title):
        sns.set(style="whitegrid")
        data_frame = pd.melt(df, id_vars='diagnosis', value_vars=columns)
        plt.figure(figsize=(12, 6))
        res=sns.boxplot(x='variable', y='value',hue='gender', data=data_frame,palette=["gold", "purple"])
        plt.title(title, size=18, fontweight='bold')
        res.set_xticklabels(res.get_xmajorticklabels(), fontsize = 15)
        res.set_yticklabels(res.get_ymajorticklabels(), fontsize = 15)
        plt.show()