imie="Janek"
# J a n e k
# 0 1 2 3 4 (klasyczne indeksowanie „od zera”)
print("Długość napisu 'Janek' to:", len(imie) )

# Klasyczny zakres "od...do"
print("imie[3:5] ", imie[3:5])  #(od indeksu 3. do 4.)

# Instrukcje równoważne (zakres od początku do pewnej pozycji):
print("imie[:4] ", imie[:4]) #(od indeksu 0. do 3.)
print("imie[0:4]", imie[0:4])

# Instrukcje równoważne (zakres od pewnej pozycji do końca):
print("imie[3:]", imie[3:])
print("imie[3:5]", imie[3:5])

# Cały zakres (od początku do końca)
print("imie[:] ", imie[:])

# Indeksy ujemne oznaczają liczenie od końca, ostatnia pozycja to... –1:
# J a n e k
# -5 -4 -3 -2 -1
print("imie[-4,-2,] ", imie[-4:-2])

moje_pi=3.14159265
pi_jako_napis=str(moje_pi) # Deklaracja zmiennej pi_jako_napis
print("Długość napisu moje_pi to: ", len(pi_jako_napis))


#Zamiana napisów na listy elementów
tytul="Alicja w krainie czarów"
slowa=tytul.split(" ")
print(tytul)
print(slowa)