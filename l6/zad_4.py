import numpy as np
import math as mt
from scipy.integrate import simps

def fzc(x):
    return mt.cos(2*mt.pow(mt.cos(x),-1))

f2=np.vectorize(fzc) #naprawa błędu 'only size-1 arrays can be converted to Python scalars'

a=-1
b=1
s=2

for i in range(10):
    s*=2 #żeby mieć parzystą liczbę podprzedziałów num nie powinno być nieparzyste
    zx=np.linspace(a,b,num=s+1, endpoint=True)
    zy=f2(zx)
    ws1=simps(zy,zx)
    print("%4d  %18.15f" %(s+1,ws1))