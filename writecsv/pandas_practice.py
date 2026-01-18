import pandas as pd
import numpy as np

csv1 = pd.read_csv("hotel_bookings.csv")
csv1.index
csv1.columns
print(csv1.describe())
print(csv1.head())

print(csv1.info())
print(csv1.tail())

print(csv1.shape)
print(type(csv1)
)
print(csv1.index.array)
print(csv1.columns.array)

csv1.to_numpy()
print(csv1.to_numpy())

csv1.to_dict()
print(csv1.to_dict())

v = np.array(csv1)
print(v)

csv1.sort_index(axis=0,ascending=False)
print(csv1.sort_index(axis=0,ascending=False))

csv1.sort_values(by="is_canceled",ascending=False)
print(csv1.sort_values(by="is_canceled",ascending=False))

csv1.loc[0, "symbol"] = "hfvjhf"
print(csv1["symbol"])

csv1.loc[0:5, "symbol"] = "hfvjhf"
print(csv1["symbol"])

