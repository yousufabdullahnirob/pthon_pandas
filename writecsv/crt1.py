import pandas as pd
dis = pd.DataFrame ({
     "a": [28, 22, 34, 42],
     "b": [28, 22, 34, 42],
     "c": [28, 22, 34, 42],
})

d = pd.DataFrame(dis)
d.to_csv("dis.csv", index=False,header = ["a","b","c"])
