# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:15:03 2019

@author: mateu
"""
#liczba maszynowa i blad wzgledny
import math

def float_to_bin(number, places = 23): 
   #Zamieniamy liczbe na str w celu rozdzielenia
   #funkcja split rozdziela liczbe calkowita 
   #i jej czesc dziesietna
    overall, fraction = str(number).split(".")
    #przechowujemy powyzsze wartosci w dwoch zmiennych
    #i z powrotem konwersja na tym int
    overall = int(overall) 
    fraction = int (fraction)  
    #zamieniamy pierwsza zmienna na typ binarny
    #usuwamy z niego przedrostek 0b
    result = bin(overall).lstrip("0b") + "."  
    #powtarzamy petle tyle razy ile chcemy miejsc po przecinku
    #w pętli wysyłamy częsc dziesiatna liczby do kolejnej funkcji
    #tam jest dzielona aż do momentu, gdy nie będzie mniejsza od 1
    #nastepnie mnozymy razy 2 i oddzielamy częsc przed przecinkiem
    for x in range(places): 
        overall, fraction = str((conversion(fraction)) * 2).split(".")
        fraction = int(fraction)
        result += overall
    #obliczanie bledu wzglednego
    temp=str(result.replace('.',''))
    wb=int(temp,2) #wartosc binarna po konwersji
    wb=conversion(wb)
    delta=math.fabs(n-wb) #wblad bezwgledny
    sigma=delta/math.fabs(n)#blad wzgledny
    print("Postac binarna:",result)
    print("Blad wzgledny tego przyblizenia: %0.2f" %(sigma*100))
  

def conversion(num):  
    while num > 1: 
        num /= 10
    return num 
  
n=2/7  
float_to_bin(n)
 
