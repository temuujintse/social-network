
import pandas as pd

url = "https://raw.githubusercontent.com/datasets/sna-datasets/main/edges.csv"
data = pd.read_csv(url)
data.to_csv("data/edges.csv", index=False)
