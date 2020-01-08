# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:06:10 2019

@author: mateu
"""

#Metoda Newtona


#Program liczący pierwiastek piątego stopnia za pomocą metody Newtona

def f(x,num): #funkcja pierwiastkowa
    return x**5-num
def f_prim(x): #pochodna pierwszej funkcji
    return 5**x

num=float(input("Enter a value:"))
x0=num-1 #przyblizamy x0 do liczby bliskiej szukanej
for i in range(1000): #iloć iteracji = dokładnosc
    temp=x0-(f(x0,num)/f_prim(x0))
#    print(temp)
    x0=temp
    
print(temp) #wypisujemy ostatnią wartosc bedaca najbardziej prawidlowa