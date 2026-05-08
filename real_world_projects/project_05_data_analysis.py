# ============================================
# REAL-WORLD PROJECT 05 — Data Analysis 📊
# Difficulty: Hard
# ============================================
# Use Python's most popular data science libraries to analyse
# a real dataset and extract meaningful insights.
#
# Dataset: Titanic passenger data (classic data science dataset)
# Download from: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
# Or use the requests library to fetch it directly in code.
#
# Requirements:
#   1. Load the CSV using pandas
#   2. Explore the data:
#        - How many rows and columns?
#        - What columns exist and what are their types?
#        - How many missing values per column?
#   3. Clean the data:
#        - Fill missing Age values with the median age
#        - Drop rows where Embarked is missing
#   4. Analyse and answer these questions:
#        - What was the overall survival rate?
#        - Did women survive more than men?
#        - Which passenger class had the highest survival rate?
#        - What was the average age of survivors vs non-survivors?
#        - What were the top 5 most common embarkation points?
#   5. Visualise with matplotlib:
#        - Bar chart: survival rate by gender
#        - Bar chart: survival rate by class
#        - Histogram: age distribution of passengers
#
# Skills used: pandas, matplotlib, data cleaning, groupby, statistics
#
# Setup:
#   pip install pandas matplotlib requests
#
# BONUS:
#   - Calculate the correlation between Fare and survival
#   - Plot a heatmap of missing values using seaborn
#   - Save all charts as PNG files
#
# Hint — getting started with pandas:
#   import pandas as pd
#   import matplotlib.pyplot as plt
#
#   df = pd.read_csv("titanic.csv")
#   print(df.head())              # first 5 rows
#   print(df.info())              # column types + nulls
#   print(df.describe())          # stats summary
#   print(df["Survived"].mean())  # survival rate
#
#   # Group by gender:
#   df.groupby("Sex")["Survived"].mean()
#
#   # Plot:
#   df["Age"].hist()
#   plt.show()
#
# Example output:
#   === Titanic Analysis ===
#   Total passengers : 891
#   Survival rate    : 38.4%
#   Female survival  : 74.2%
#   Male survival    : 18.9%
#   Class 1 survival : 63.0%
#   Class 2 survival : 47.3%
#   Class 3 survival : 24.2%
#   Avg age (survived)     : 28.3
#   Avg age (not survived) : 30.6
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import requests
import os

DATASET_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
CSV_FILE = "titanic.csv"


# YOUR CODE HERE:
