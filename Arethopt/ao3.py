import pandas as pd
var = pd.DataFrame ({
     "a": [28, 22, 34, 42],
     "b": [28, 22, 34, 42],
     "c": [28, 22, 34, 42],
})
var ["sum"] = var ["a"] + var ["b"] + var ["c"]
print(var["sum"])

var ["sub"] = var ["a"] - var ["b"] - var ["c"]
print(var["sub"])

var ["mul"] = var ["a"] * var ["b"] * var ["c"]
print(var["mul"])

var ["div"] = var ["a"] / var ["b"] / var ["c"]
print(var["div"])

var ["compare"] = (var ["a"] == var ["b"]) & (var ["b"] == var ["c"])
print(var["compare"])

