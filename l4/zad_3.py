import math
from scipy import optimize

u=2510
M0=2.8*(10**6)
m=13.3*(10**3)
g=9.81

def f(t):
    return u*math.log(M0/(M0-m*t))-g*t-335

print("t=",optimize.newton(f,0))


    