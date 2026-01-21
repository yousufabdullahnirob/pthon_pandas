import pandas as pd

var = pd.read_csv("hotel_bookings.csv")
print(var.head())

var.dropna(subset=["agent","company"], inplace=True)
print(var.isnull().sum())
