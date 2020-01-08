from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import numpy as np

ax1=np.array([1.0,2.5,3.5,4.0,1.1,1.8,2.2,3.7],dtype=float)
ay1=np.array([6.008,15.722,27.13,33.772,5.257,9.549,11.098,28.828])
wiel=lagrange(ax1,ay1)
aw=np.polyfit(ax1,ay1,1)
axd=np.arange(0.9,4.1,0.01)
paw_1=np.poly1d(aw)
plt.plot(ax1,ay1,'o')
plt.plot(axd,wiel(axd))
plt.plot(axd,paw_1(axd))
plt.legend(['dane','interpol,','aproks.'],loc='best')
plt.show()