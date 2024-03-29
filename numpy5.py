import numpy as np
t=np.arange(10) # Tablica [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (zawiera 10 elementów)
t1=t[:3] # Wycinek [0,2], tj. pierwsze 3 wartości, tj. [0 1 2]
t2=t[3:] # Wycinek [2,9], tj. pozostałe 7 wartości, tj. [3 4 5 6 7 8 9]
t3=t[5:7] # Wycinek [5,6], tj. zakres w środku, tj. [5 6]
t4=t[::3] # Co trzeci element, tj. [0 3 6 9]
t5=t[4::2] # Co drugi element, zaczynając od indeksu 4, tj. [4 6 8]
t6=t[::-1] # Wszystkie wartości, ale od końca (odwracamy tablicę), tj. [9 8 7 6 5 4 3 2 1 0]
t7=t[4::-2] # Wszystkie co drugie wartości, od końca i zaczynając od indeksu 4, tj. [4 2 0]

v=np.array( [ [1, 2, 3, 4, 5],
[5, 6, 7, 8, 9],
[9, 10, 11, 12, 13],
[14, 15, 16, 17, 18],
] )


v1=v[:2, :4]

# Wycinek 3 wiersze x (co 2 kolumny)
v2=v[:3, ::2]

# Wycinek 3 wiersze x (co 2 kolumny)
v2=v[:3, ::2]