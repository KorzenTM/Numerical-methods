# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:27:48 2019

@author: mateu
"""
#Obliczanie predkosci ze wzoru
import math

#v=335 #prędkosc dzwieku
u=2510 #predkosc spalin wzgledem rakiety
M0=2.8E6 #masa rakiety w momencie startu
m=13.3E3 #szybkosc zuzycia paliwa
g=9.81 #przyspiesznie ziemskie
t=0 #poczatkowa wartosc
v=0

while v<335.0:
    t+=1
    v=u*math.log(M0/(M0-m*t))-g*t
 #   print(v,t)

print("Predkosc dzwieku zostanie osiagnieta po:",t,"sekundach")


    