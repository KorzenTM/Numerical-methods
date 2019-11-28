from scipy.integrate import trapz
import numpy as np
import math as mh

def fzc(x):
    return (mh.cos(x)-mh.exp(x))/(mh.sin(x))


f2=np.vectorize(fzc)
a=-1
b=1
s=2

for i in range(10):
    s*=2
    zx=np.linspace(a,b,num=s,endpoint=True)
    zy=f2(zx)
    wt2=trapz(zy,zx)
    print("%4d  %18.15f" %(s,wt2))