# Libraries needed for the tutorial
import inline as inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# to attach the csv file on GitHub

import requests
import io

# downloading the csv file from your GitHub account

url = "https://raw.githubusercontent.com/ine-rmotr-curriculum/FreeCodeCamp-Pandas-Real-Life-Example/master/data/sales_data.csv"
download = requests.get(url).content

# reading the downloaded content and turning it into a pandas dataframe

sales = pd.read_csv(url)

sales.head()  # putting into dataframe which has restricted data type of each column
sales.shape # telling how many rows and columns our dataframe has
sales.info()  # tell us the summarized information of columns (data type, title)
sales.describe() # tell us the min, max, mean, etc. of each category

def description():
    description = sales.describe()
    print(description)

# examples of different plots

sales['Unit_Cost'].mean()
sales['Unit_Cost'].median()

# 1. Box plot: To point out anomalous points
def box_plot():
    sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))
    plt.show()

# 2. Density plot: To see the whole plot
def density_plot():
    ax = sales['Unit_Cost'].plot(kind = 'density', figsize=(14,6))
    #to plot mean and median in density plot
    ax.axvline(sales['Unit_Cost'].mean(), color = 'red')
    ax.axvline(sales['Unit_Cost'].median(), color = 'green')
    plt.show()

# 3. Histogram
def histogram():
    ax = sales['Unit_Cost'].plot(kind= 'hist', figsize = (14,6))
    ax.set_ylabel('Number of sales')
    ax.set_xlabel('dollars')
    plt.show()

# 4. Pie chart: To express categorical data
def pie_chart():
    sales['Age_Group'].value_counts()  # count the number of items in each category, this is not given, so python can plot
    sales['Age_Group'].value_counts().plot(kind= 'pie', figsize=(6,6))
    plt.show()
    print(sales['Age_Group'].value_counts())

# 5. Bar chart: To express categorical data
def bar_chart():
    ax = sales['Age_Group'].value_counts().plot(kind= 'bar', figsize=(14,6))
    ax.set_ylabel('Number of sales')

# 6. Correlation Matrix: To show relationship between categories
def matrix():
    corr = sales.corr()  # formula to express correlation between categories
    print(corr)
    # now illustrate these by graph
    # dark red indicates strong negative correlation, dark blue indicates strong positive indication

    fig = plt.figure(figsize=(8,8))
    plt.matshow(corr, cmap = 'RdBu', fignum = fig.number)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation = 'vertical')
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.show()

# 7. Scatter plot: If it's just between 2 categories, this can also express the correlation scatteredly
def scatter_plot():
    sales.plot(kind = 'scatter', x = 'Customer_Age', y = 'Revenue', figsize=(6,6))
    plt.show()

# 8. Combination of boxplot of the categorical items versus another category
def combo_plot():
    ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(10,6))
    ax.set_ylabel('Profit')
    plt.show()

    # how to plot all boxplots at once:
    boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit']
    sales[boxplot_cols].plot(kind = 'box', subplots = True, layout = (2,3), figsize = (14,8))
    plt.show()

