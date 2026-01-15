import pandas as pd
var = pd.DataFrame({"name": ["John", "Anna", "Peter", "Linda"],
     "age": [28, 22, 34, 42],
     "city": ["New York", "Paris", "Berlin", "London"]
     })
print(var)
print(type(var))
print(var.shape)
print(var.head())
print(var.tail())

