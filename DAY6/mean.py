import numpy as np
marks=np.array([[60,70,30],[31,24,56],[68,90,58]])
print(marks)
print(np.mean(marks))
print("shape:",marks.shape)
row=np.mean(marks,axis=1)
print(row)
column=np.mean(marks,axis=0)
print(column)