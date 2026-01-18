import pandas as pd
import numpy as np

csv1 = pd.read_csv("hotel_bookings.csv")

csv1.loc[0, "symbol"] = 1
print(csv1["symbol"])

csv1.loc[0:5, "symbol"] = 1
print(csv1["symbol"])

csv1.iloc[0, 1] = 1
print(csv1["is_canceled"])

csv1.drop(columns=["symbol"], inplace=True)
print(csv1)

