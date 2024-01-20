import numpy as np
t=np.array( [ [3, 9, 1], [ -2, 2, 6] ] ) # Dwuwymiarowa
print( t.min() )


t1=np.array( [ [3, 9, 1], [ -2, 2, 6] ] ) # Dwuwymiarowa
t2=np.array( [ 3, 9, 1, -2, 2, 6] ) # Jednowymiarowa
tsort1=np.sort(t1) # Zwróci [[ 1 3 9], [-2 2 6]]
tsort2=np.sort(t2) # Zwróci [ -2 1 2 3 6 9 ]


t = np.array( [5, 10, 15, 20] )
print("t + 5 =", t + 5) # [ 5 10 15 20]
print("t - 5 =", t - 5) # [10 15 20 25]
print("t * 2 =", t * 2) # [10 20 30 40]
print("t / 2 =", t / 2) # [ 2.5 5. 7.5 10. ]
print("t // 2 =", t // 2) # [ 2 5 7 10]
print("-t = ", -t) # [ -5 -10 -15 -20]
print("t ** 2 = ", t ** 2) # [ 25 100 225 400]
print("t % 2 = ", t % 2) # [1 0 1 0]


mojekaty = np.array( [0, 30, 45, 60, 90, 180, 270, 360] )
sinusy=np.sin(mojekaty*np.pi/180) # Konwersja z kątów 0... 360 stopni na radiany
cosinusy=np.cos(mojekaty*np.pi/180) # Jw.
tangensy=np.tan(mojekaty*np.pi/180) # Jw.
# Oto kilka pozostałych klasycznych funkcji często używanych w praktyce przetwarzania
# danych (składnia użycia jak w przykładzie wyżej):
t1 = np.array([5, 10, 15, 20])
t2 = np.array([2, 1, 2, 4])
t3 = np.array([9, 16, 8, 81])
print(np.negative(t1)) # Negacja: [ -5 -10 -15 -20]
print(np.add(t1, t2)) # Dodawanie: [ 7 11 17 24]
print(np.subtract(t1, t2)) # Odejmowanie: [ 5 10 15 20]
print(np.multiply(t1, t2)) # Mnożenie: [14 11 34 96]
print(np.divide(t1, t2)) # Dzielenie: [ 3.5 11. 8.5 6. ]
print(np.power(t1, t2)) # Potęgowanie: [ 25 10 225 160000]
print(np.sqrt(t3)) # Pierwiastek kwadratowy: [3. 4. 2.82842712 9. ]