# Ch1 - Uploading Data
import pandas as pd

data = pd.read_csv("C:/Users/jsmith/my_data.csv")

data.head(20) # prints out first 20 rows of data

data.describe() # gives quick descriptive stats on each in columns
