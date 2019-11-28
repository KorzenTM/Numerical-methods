from scipy.special import roots_legendre
import numpy as np
import math as mh


def fzc(x):
    return mh.log(x)/(x**2-2*x+2)

a=1
b=mh.pi
s=2

for n in range(3,15):
    xi,ai=roots_legendre(n)
    I_n=0
    for i in range(len(ai)):
        I_n+=(b-a)/2*ai[i]*fzc((b+a)/2+(b-a)/2*xi[i])
    print("%4d  %18.15f" %(n,I_n))