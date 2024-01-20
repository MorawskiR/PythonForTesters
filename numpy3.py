import numpy as np
t1 = np.arange(1,11) # Wstępna deklaracja tablicy jednowymiarowej (seria liczb od 1. do 10.)
t1=t1.reshape( (2,5) )
print(t1)


t8 = np.arange(1,11) # Jednowymiarowa, typ domyślny, seria liczb od 1. do 10.
print("t8=", t8)
t8.resize(4,5) # Rozszerzenie z 10 elementów na 4x5, czyli 20
print("t8 po resize (4,5) =", t8)


t=np.array([ [-2, 1, 7], [4, -5, 9], [2, 0, 3] ])
print(t)
print("Spłaszczanie wierszami:",t.ravel(order='C')) # Tryb domyślny, parametr można ominąć
print("Spłaszczanie kolumnami:",t.ravel(order='F'))