import matplotlib.pyplot as plt
import numpy as np

ccx=[0,1.525,3.05,4.575,6.1,7.625,9.150]
ccy=[1,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741]

fk1=np.polyfit(ccx,ccy,2)
wiel=np.poly1d(fk1)
xx=np.linspace(0,10,num=100,endpoint=True)
plt.plot(xx,wiel(xx))
plt.plot(ccx,ccy,'o')
plt.show()

print("p(10.5)=",wiel(10.5))