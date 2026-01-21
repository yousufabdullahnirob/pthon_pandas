import pandas as pd

var = pd.read_csv("hotel_bookings.csv")

print("Original Shape:", var.shape)
print("\nMissing values per column:")
print(var.isnull().sum())


var_dropped = var.dropna(axis=0)
print("\nShape after dropna (rows):")
print(var_dropped.shape)
print(var_dropped)


var_filled = var.fillna("python")
print("\nShape after fillna('python'):")
print(var_filled.shape)
print(var_filled)

var.ffill(inplace=True)
print(var)


