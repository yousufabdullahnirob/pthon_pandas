import pandas as pd

var = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

var1 = pd.DataFrame({"C": [11, 22, 33], "B": [4, 5, 6]}) 

result = pd.merge(var, var1, on="B", how="inner")

print(result)
