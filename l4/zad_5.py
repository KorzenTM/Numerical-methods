#Trajectory 

import numpy as np
import matplotlib.pyplot as plt
import math

height = 2 #basketplayer height
distance = 10 #distance to basket
basket_height = 3 #basket height
g = 9.81 #acceleration
angle = 45 #desired angle

def x(v0,alfa,t):
    return (v0*np.cos(alfa)*t)
def y(v0,alfa,t):
    return (2+v0*np.sin(alfa)*t-((g*t**2)/(2)))






