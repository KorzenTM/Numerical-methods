# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:51:45 2019

@author: mateu
"""

import numpy as np
coeff=[1,complex(5,1),complex(8,-5),complex(30,-14),-84]
roots=np.roots(coeff)
for i in range(0,len(roots)):
    print("x0(",i,")=",roots[i])