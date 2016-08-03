# Ch1 - Uploading Data
import pandas as pd

data = pd.read_csv("C:/Users/jsmith/my_data.csv")

print(data.head(20)) # prints out first 20 rows of data

print(data.describe()) # gives quick descriptive stats on each in columns

print(data.dtypes) # lists each column and current data types (e.g. int, float, date)


# Ch4 - Visualizing Data
%matplotlib inline # only if you're using Jupyter

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

city_groups = data.groupby('city').size()
city_groups.hist()
