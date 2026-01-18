import pandas as pd

csv1 = pd.read_csv("hotel_bookings.csv")
csv1.index
csv1.columns
print(csv1.head())