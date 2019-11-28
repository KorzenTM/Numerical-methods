import numpy as np
import math as mh
from scipy.integrate import simps

def fzc(x,x0):
    return 1/mh.sqrt(1-mh.pow(mh.sin(np.radians(x0/2)),2)*mh.pow(mh.sin(np.radians(x)),2))

f2=np.vectorize(fzc) #naprawa błędu 'only size-1 arrays can be converted to Python scalars'
a=0
b=mh.pi/2
s=2
angle=[0,15,30,45] #angle

for i in angle:
    print(i)
    s=2
    for j in range(10):
        s*=2 #żeby mieć parzystą liczbę podprzedziałów num nie powinno być nieparzyste
        zx=np.linspace(a,b,num=s+1, endpoint=True)
        zy=f2(zx,i)
        ws1=simps(zy,zx)
        print("%4d  %18.15f" %(s+1,ws1))