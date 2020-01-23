import numpy as np
from scipy.linalg import eigh

A=np.array([[-1,-4,1],[-1,-2,-5],[5,4,3]],dtype=float)
print(A)
w1,v1=eigh(A)
print("Wartości własne:")
print(w1)
print("\n wektory własne:")
print(v1)