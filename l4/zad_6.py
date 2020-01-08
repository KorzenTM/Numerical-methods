
import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

def f(x):
    return [np.tan(x[0])-x[1]-1,
            np.cos(x[0])-3*np.sin(x[1])]

ax = plt.axes(projection="3d")
x=np.arange(-10,10,0.1)
y=np.arange(-10,10,0.1)
X,Y = np.meshgrid(x,y)
Z1=np.tan(X)-Y-1
Z2=np.cos(X)-3*np.sin(Y)
ax.plot_surface(X,Y,Z1)
ax.plot_surface(X,Y,Z2)
plt.show()

sol=[]

for a in np.arange(0, 1.5, 0.01):
	for b in np.arange(0, 1.5, 0.01):
		x0 = np.array([a,b])
		x1 = optimize.root(f, x0)
		if x1.success:
			if(x1.x[0]>=0 and x1.x[0]<=1.5):
				x1.x[0] = round(x1.x[0], 7)
				if x1.x[0] not in sol:
					print(x1.x)
					sol.append(x1.x[0])
                    