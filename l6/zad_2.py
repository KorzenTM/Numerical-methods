import numpy as np
import math as mh
import matplotlib.pyplot as plt
from scipy.misc import derivative
from scipy.interpolate import lagrange,CubicSpline

x0=0.2
dx=np.array([0.0,0.1,0.2,0.3,0.4])
dy=np.array([0.0,0.078348,0.13891,0.192916,0.244981])

#plt.plot(dx,dy,'o')
#plt.show()

wl=lagrange(dx,dy)
print("wl=",wl)
pw1=np.polyder(wl) #zwraca pochodna wielomianu
tcs=CubicSpline(dx,dy) #interpolacja CubicSpline
fw2=np.polyfit(dx,dy,3) #fitowanie wielomianem 3 stopnia
print("\nwf=",np.poly1d(fw2))
pfw2=np.polyder(np.poly1d(fw2))

print("\npwl:",pw1(x0))
print("pcs:",tcs(x0,1))
print("pwf:",pfw2(x0))

