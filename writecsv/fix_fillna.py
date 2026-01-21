import pandas as pd

# Load the dataset
# Assuming the file path from your previous scripts
var = pd.read_csv(r"D:\hotel_bookings.csv")

# Correct way to fill specific column 'is_canceled' with value 'python'
# Using a dictionary: {"column_name": "value"}
var_filled = var.fillna({"is_canceled": "python"})

print("Filled shape:", var_filled.shape)
print(var_filled.head())
