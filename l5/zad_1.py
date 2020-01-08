from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import numpy as np

dx=np.array([0,3,6],dtype=float)
dy=np.array([1.225,0.905,0.652],dtype=float)
wl=lagrange(dx,dy)
plt.plot(dx,dy,'o')
xw=np.arange(-1,8,0.1)
plt.plot(xw,wl(xw))
plt.xlabel('x')
plt.ylabel('w')
plt.show()
