import numpy as np
dict = {}
dict["AA"] = 1
print dict["AA"]

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])
d = np.concatenate((a,b,c), axis=0)
print a
print b
print d
