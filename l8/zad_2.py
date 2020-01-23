import numpy as np
from scipy.linalg import eigh,hilbert

n=6
A=hilbert(6)
print("Macierz Hilberta 6x6:",A)
w1,v1=eigh(A)
print("Wartości własne:")
print(w1)
print("\n wektory własne:")
print(v1)
