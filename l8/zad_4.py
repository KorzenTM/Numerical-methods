import numpy as np
from scipy.linalg import eigh_tridiagonal,eigh
import matplotlib.pyplot as plt

l=0.2
a=4.6

m1=100
m2=1000

i1=np.arange(0,m1,1)
i2=np.arange(0,m2,1)

h1=2*a/m1
h2=2*a/m2

x1=-a+i1*h1
x2=-a+i2*h2

d1=((1/h1**2)+(x1**2/2)+l*x1**4)*np.ones(m1)
nd1=-(1/(2*h1**2))*np.ones(m1-1)
w1,v1=eigh_tridiagonal(d1,nd1)

d2=((1/h2**2)+(x2**2/2)+l*x2**4)*np.ones(m2)
nd2=-(1/(2*h2**2))*np.ones(m2-1)
w2,v2=eigh_tridiagonal(d2,nd2)
#pierwsze 4 wartośći własne
print("m=100\n")
print("wartości własne")
print(w1[:4])
#pierwsze 4 wektory własne
print("\n wektory własne")
print(v1[:,:4])
#pierwsze 4 wartośći własne
print("m=1000\n")
print("wartości własne")
print(w2[:4])
#pierwsze 4 wektory własne
print("\n wektory własne")
print(v2[:,:4])

plt.subplot(121)
plt.title("m=100")
plt.grid()
plt.plot(i1,v1)
plt.subplot(122)
plt.title("m=1000")
plt.grid()
plt.plot(i2,v2)
plt.show()

