import pandas as pd

var = pd.read_csv("hotel_bookings.csv")

# Check for missing values
print("Original Shape:", var.shape)
print("\nMissing values per column:")
print(var.isnull().sum())

# Drop rows with missing values
# axis=0 drops rows, axis=1 drops columns
# how='any' drops if any NA, how='all' drops if all NA
var_dropped = var.dropna(axis=0)
print("\nShape after dropna (rows):")
print(var_dropped.shape)
print(var_dropped)

# Fill missing values
# simple fill with a value
var_filled = var.fillna("python")
print("\nShape after fillna('python'):")
print(var_filled.shape)
print(var_filled)

# Fill with specific logic (commented out example)
# var.fillna({'column_name': 0}, inplace=True)
