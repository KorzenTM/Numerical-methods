import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d,CubicSpline

dx=np.array([0.2,2,20,200,2000,20000],dtype=float)
dy=np.array([103,13.9,2.72,0.8,0.401,0.433],dtype=float)

log_x=np.log10(dx)
log_y=np.log10(dy)
cs=CubicSpline(log_x,log_y)
xs=np.linspace(-1,5,num=100,endpoint=True)
plt.plot(log_x,log_y,'o')
plt.plot(xs,cs(xs))
plt.show()

print("cd(5.50)=",10**cs(np.log10(5.50)))
print("cd(5000)=",10**cs(np.log10(5000)))






