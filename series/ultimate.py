#series
import pandas as pd ;
x = [5,56,44,3,56,53,35,4]

var = pd.Series(x,index=[1,2,3,4,5,6,7,8],dtype="float")
print(var)
print(var.values)
print (type(var))
print (var.index)
print (var.dtype)
print (var.size)
print (var.ndim)
print (var.shape)
print (var.nbytes)
print (var[2])
