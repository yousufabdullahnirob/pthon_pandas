import pandas as pd

var = pd.read_csv(r"D:\hotel_bookings.csv")

var_filled = var.fillna({"is_canceled":     "python"})

print("Filled shape:", var_filled.shape)
print(var_filled.head())
