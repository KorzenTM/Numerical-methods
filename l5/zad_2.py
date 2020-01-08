from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

dx=np.array([1,1.25,1.5,1.75,2,2.25,2.5,2.75,3],dtype=float)
dy=np.array([-0.5403,-0.0104,0.9423,1.7445,1.3073,-0.7718,-2.4986,-0.7903,2.7334],dtype=float)
cs=CubicSpline(dx,dy)
plt.plot(dx,dy,'o')
xd1=np.linspace(0.9,3.1,num=150,endpoint=True)
plt.plot(xd1,cs(xd1))
plt.plot(xd1,cs(xd1,1))
plt.legend(['dane','cs','1 der'], loc='best')
plt.show()

print("Pierwiastki:")
pierw=cs.roots(0.9,3.1)
for r in pierw:
    print("%12.8f %12.8f" %(r,cs(r)))
print("y'(2.1)=",cs(2.1,1))