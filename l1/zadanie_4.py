# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:58:15 2019

@author: mateu
"""

#macierze hilberta

from scipy import linalg

hilbert_4=linalg.hilbert(4)
hilbert_8=linalg.hilbert(8)

print("Macierz Hilberta 4x4:\n\n",hilbert_4)
print("Macierz Hilberta 4x4 po odwroceniu:\n\n",linalg.inv(hilbert_4))
print("Macierz Hilberta 8x8:\n\n",hilbert_8)
print("Macierz Hilberta 8x8 po odwroceniu:\n\n",linalg.inv(hilbert_8))

for n in range(5,21):
   hilbert=linalg.hilbert(n)
   det=linalg.det(hilbert)
   print("Wyznacznik macierzy Hilberta",n,"x",n,"wynosi:",det)
