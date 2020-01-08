# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:38:00 2019

@author: mateu
"""

#norma i wskaźnik uwarunkowania

from scipy import linalg
#macierze hilberta przed i po odwróceniiu
hilbert_5=linalg.hilbert(5)
hilbert_5_inv=linalg.inv(hilbert_5)
norm_5=linalg.norm(hilbert_5,np.inf)
norm_5_inv=linalg.norm(hilbert_5_inv,np.inf)

hilbert_10=linalg.hilbert(10)
hilbert_10_inv=linalg.inv(hilbert_10)
norm_10=linalg.norm(hilbert_10,np.inf)
norm_10_inv=linalg.norm(hilbert_10_inv,np.inf)

hilbert_20=linalg.hilbert(20)
hilbert_20_inv=linalg.inv(hilbert_20)
norm_20=linalg.norm(hilbert_20,np.inf)
norm_20_inv=linalg.norm(hilbert_20_inv,np.inf)

print("Norma macierzy Hilberta 5x5:",norm_5)
print("Wskaźnik uwarunkowania:",norm_5_inv*norm_5)
print("Norma macierzy Hilberta 10x10:",norm_10)
print("Wskaźnik uwarunkowania:",norm_10_inv*norm_10)
print("Norma macierzy Hilberta 20x20:",norm_20)
print("Wskaźnik uwarunkowania:",norm_20_inv*norm_20)

