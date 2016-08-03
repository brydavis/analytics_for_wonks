# Ch1 - Uploading Data
import pandas as pd

data = pd.read_csv("C:/Users/jsmith/my_data.csv")

print(data.head(20)) # prints out first 20 rows of data

print(data.describe()) # gives quick descriptive stats on each in columns

print(data.dtypes) # lists each column and current data types (e.g. int, float, date)
