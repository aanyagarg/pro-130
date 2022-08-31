import pandas as pd

data = pd.read_csv("pro130/Final.csv")


del data["Star_name"]


data = data.dropna()


data.to_csv("pro130/Data.csv")