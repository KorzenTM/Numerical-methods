import numpy as np
from scipy.linalg import eigh_tridiagonal,eigh

n1=10
d1=2*np.ones(n1)
nd1=-1*np.ones(n1-1)
w1,v1=eigh_tridiagonal(d1,nd1)
n2=10
d2=2*np.ones(n2)
nd2=-1*np.ones(n2-1)
w2,v2=eigh_tridiagonal(d2,nd2)
#pierwsze 3 wartośći własne
print("n=10\n")
print("wartości własne")
print(w1[:3])
#pierwsze 3 wektory własne
print("\n wektory własne")
print(v1[:,:3])
#pierwsze 3 wartośći własne
print("n=100\n")
print("wartości własne")
print(w2[:3])
#pierwsze 3 wektory własne
print("\n wektory własne")
print(v2[:,:3])


