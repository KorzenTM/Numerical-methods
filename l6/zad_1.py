import numpy as np
import math as mh
from scipy.misc import derivative



def f(x):
    return mh.log(np.tanh(x/(x**2+1)))
def p1f(x):
    return (-(2*(x**2-1)*1/(mh.sinh(2*x/(x**2+1))))/((x**2+1)**2))
x0=0.2
h=0.10
ep1=p1f(x0)
print("First:")
for i in range(14):
    h/=10
    np1=derivative(f,x0,dx=h,order=5)
    print("h=%7.1e  f'=%16.12f  df'=%13.6e" %(h,np1,ep1-np1))

h=1.0e-04 #dokładne przybliżenie h
print("f'(x0)=:",derivative(f,x0,dx=h,order=5))
print("f''(x0)=:",derivative(f,x0,dx=h,n=2,order=5))
print("f'''(x0):",derivative(f,x0,dx=h,n=3,order=5))