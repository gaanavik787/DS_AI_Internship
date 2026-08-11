import pandas as pd
import numpy as np
x=[1,2,3,4,5]
y=pd.Series(x)
print(y)

x=np.array([10,20,30,40,50])
y=pd.Series(x)
print(y)

x={'a':10,'b':20,'c':30,'d':40,'e':50}
y=pd.Series(x)
print(y)

z={'name':'Alice', 'age':25, 'city':'New York'}
y=pd.Series(z)
print(y)

marks=[28,45,78]
x=pd.Series(marks,index=["maths","science","english"])

print(x)
print(x.index.tolist())

import pandas as pd

marks = pd.Series(
    [85, 90, 78, 88],
    index=["Python", "Java", "Maths", "DBMS"]
)

print(marks)
print(marks[["Python","Maths"]])
print(marks[marks>80])

print("python marks:", marks["Python"])
print(y.index[2],":",y.iloc[2])

scores = pd.Series([75, 85, 90, 80, 95])
passed = scores[scores <= 60]
print(passed)

data=pd.Series([10,None,30,None])
print(data.isnull())
print(data.fillna(0))
