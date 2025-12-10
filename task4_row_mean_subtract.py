import numpy as np
arr=np.array([[11,22,33],[44,55,66],[77,88,99]])
b=arr.mean(axis=1,keepdims=True)
print(b)
c=arr-arr.mean(axis=1,keepdims=True)
print(c)
