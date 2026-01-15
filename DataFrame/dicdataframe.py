import pandas as pd

d = {"name": ["John", "Anna", "Peter", "Linda"],
     "age": [28, 22, 34, 42],
     "city": ["New York", "Paris", "Berlin", "London"]}
var1 = pd.DataFrame(d)
print(var1)
print(type(var1))
var = pd.DataFrame(d)
print(d)


