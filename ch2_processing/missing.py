# Ch1 - Uploading Data
import pandas as pd

data = pd.read_csv("C:/Users/jsmith/my_data.csv")

# Ch2 - Filling in Missing Values

data["race"] = data["race"].fillna("Unknown")

data.head(20)
