# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:22:35 2019

@author: mateu
"""

import matplotlib.pyplot as plt
import numpy as np

xt=np.arange(0,1.5,0.01)
function_1=np.cos(xt)-3*np.sin(np.tan(xt)-1)
function_2=xt*0
lab1="f(x)=cos(x)-3sin(tg(x)-1)"
lab2="f(x)=0"
plt.plot(xt,function_1, label=lab1)
plt.plot(xt,function_2,label=lab2)
plt.xlabel('x')
plt.ylabel('f')
plt.legend()
plt.grid
plt.show()

       
       
        
        