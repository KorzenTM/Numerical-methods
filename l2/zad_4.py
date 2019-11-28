# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:42:08 2019

@author: mateu
"""

#dokladnosc obliczen(przekształcić tak by nie było odejmowania)

import numpy as np

def u1_a(x): #obliczenia w pojedynczej precyzji
    return np.sqrt(np.float32(x**4+4))-2

def u2_b(x): #obliczenia w podwójnej precyzji
    return np.sqrt(x**4+4)-2

def u3_a(x): #obliczenia w pojedynczej precyzji bez odejmowania
    return (np.float32(x**2))/(np.sqrt(np.float32(x**2+4))+2)

def u4_b(x): #obliczenia w podwójnej precyzji bez odejmowania
    return (x**2)/(np.sqrt(x**2+4)+2)

print("u1 - obliczenia w pojedynczej precyzji z odejmowanie")
print("u2 - obliczenia w podwójnej precyzji z odejmowaniem")
print("u3 - obliczenia w pojedynczej precyzji bez odejmowania")
print("u4 - obliczenia w podwójnej precyzji bez odejmowania")
print("%4s  %16s  %16s"%('x','u1','u2'))
for n in range(2,26,2):
    x=2**(-n)
#    print(n,"\t",x)
    print("%3.1e  %16.12e  %16.12e" %(x,u1_a(x),u2_b(x)))

print("%4s  %16s  %16s"%('x','u3','u4'))
for n in range(2,26,2):
    x=2**(-n)
#    print(n,"\t",x)
    print("%3.1e  %16.12e  %16.12e" %(x,u3_a(x),u4_b(x)))
