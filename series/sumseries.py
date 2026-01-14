import pandas as pd
s1 = pd.Series(12,index=[1,2,3,4,5])
print(s1)
s2 = pd.Series(12,index=[1,2,3])
print(s2)
print (s1+s2)