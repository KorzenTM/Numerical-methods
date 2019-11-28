from scipy.integrate import nquad
import numpy as np
import math as mh

def fxy(x,y):
    return mh.sin(mh.pi*x)*mh.sin(mh.pi*(y-x))
#granice całki wewnętrznej
def bondsx(z): 
    return [0,z]
#granice całki zewnętrznej
def bondsy():
    return [0,1]

wnxy=nquad(fxy,[bondsx,bondsy])
print("%18.14f"%(wnxy[0]))
