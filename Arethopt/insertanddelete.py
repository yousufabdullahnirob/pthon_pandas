import pandas as pd
var = pd.DataFrame ({
     "a": [28, 22, 34, 42],
     "b": [28, 22, 34, 42],
     "c": [28, 22, 34, 42],
})
#var.insert(1, "sum", var["a"] + var["b"] + var["c"])
#print(var)

var.insert(1,"python", var["a"])
print(var)

var["py"] = var ["a"][:3]
print(var["py"])

var.drop("py", axis=1, inplace=True)
print(var)

var ["delete"] = var.pop("python")
print(var)