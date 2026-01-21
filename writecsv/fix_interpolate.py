import pandas as pd
import numpy as np


var = pd.read_csv(r"D:\hotel_bookings.csv")

print("Original Data Head:")
print(var.head())

print("\n--- Attempting to reproduce error ---")
try:
   
    var.interpolate(method="linear", axis=1)
except TypeError as e:
    print(f"Caught expected error: {e}")

print("\n--- Applying Fix ---")

numeric_var = var.select_dtypes(include=[np.number])
interpolated_numeric = numeric_var.interpolate(method="linear", axis=1)

print("Interpolation successful on numeric columns.")

# Fix for typo 'interplote' -> 'interpolate'
print("\n--- Testing interpolate with limit ---")
# Applying to numeric columns to avoid TypeError
numeric_filled = numeric_var.interpolate(method="linear", limit_direction="forward", limit=2)

print("\n--- Testing interpolate with limit_area='inside' ---")
# 'inside' only fills NaNs that are surrounded by valid values
numeric_inside = numeric_var.interpolate(method="linear", limit_area="inside")
print(numeric_inside.head())


