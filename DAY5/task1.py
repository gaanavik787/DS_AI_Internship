import random
a=[2,4,6,8,0,1]

print(random.randint(1, 10))
print(random.random())
print(random.choice(a))
print(random.shuffle(a))


marks=[30,40,67,12]
newmarks=[]
for x in marks:
    newmarks.append(x+5)
print(newmarks)


import numpy as np
marks=np.array([12,34,78,90,59])
result=marks+5
print(result)