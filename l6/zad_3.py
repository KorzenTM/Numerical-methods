import numpy as np
import math as mh
import matplotlib.pyplot as plt
from scipy.misc import derivative
from scipy.interpolate import lagrange,CubicSpline

x0=0
dx=np.array([-2.2,-0.3,0.8,1.9], dtype=float)
dy=np.array([-15.18,10.962,1.92,-2.04], dtype=float)

wl=lagrange(dx,dy)
wl_1=np.polyder(wl)
wl_2=np.polyder(wl,m=2)
print("wl=",wl)
print("f'(0)=",wl_1(x0))
print("f''(0)=",wl_2(x0))