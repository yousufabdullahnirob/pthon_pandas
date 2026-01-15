import pandas as pd

dis = pd.read_csv("hotel_bookings.csv")
print(dis.head())

dis2 = pd.read_csv("hotel_bookings.csv",nrows=2,usecols=["hotel","is_canceled"],
dtype={"is_canceled":bool})
print(dis2.head())

dis3 = pd.read_csv("hotel_bookings.csv",skiprows=2,
dtype={"is_canceled":bool})
print(dis3.head())

dis4 = pd.read_csv("hotel_bookings.csv",
header=None).add_prefix("col")
print(dis4.head())



