import pandas as pd
var = pd.DataFrame({"name": ["John", "Anna", "Peter", "Linda"],
     "age": [28, 22, 34, 42],
     "city": ["New York", "Paris", "Berlin", "London"]
     })
var[" full"] = var["name"]+" "+var["age"].astype(str)+" "+var["city"]
print(var[" full"])

# var["fullempty"] = var["name"]-" "+var["age"].astype(str)-" "+var["city"]
# Note: String subtraction is not supported in Python. Use .str.replace() or similar methods if trying to remove characters.
# print(var["fullempty"])