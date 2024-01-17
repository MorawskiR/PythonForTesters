nazwapliku="inputs.txt"
print("*** Odczyt pojedynczych znaków ***")
try:
    plik=open(nazwapliku,"r") # Wpisz złą nazwę pliku, np. inputs.txz, aby sprawdzić wyjątki!
except FileNotFoundError:
    print("Hm, gdzie ten plik?")
    exit()
print("Otwarto plik: ",plik.name)
print("Tryb otwarcia: ",plik.mode)
print("Pozycja kursora", plik.tell())
print("4 znaki:[", plik.read(4),"]")
print("Pozycja kursora po przeczytaniu 4 znaków", plik.tell())
print("5 kolejnych znaków znaki:[", plik.read(5),"]")
print("Ostatni znak to będzie znak nowej linii:[", plik.read(1),"]") # (*)
plik.close() # Pamiętaj o zamykaniu pliku!
print("*** Odczyt pojedynczych wierszy ***")
plik = open(nazwapliku, "r")
# Czytamy tylko pierwsze 3 znaki z bieżącego wiersza:
print("Linia 1.(3 znaki):", plik.readline(3))
print("Linia 2.(pozostałe znaki):", plik.readline(), end="")
print("Linia 2.:", plik.readline(), end="")
print("Linia 3.:", plik.readline())
# Wiersz 4. nie istnieje i ta instrukcja nic nie zwróci:
print("Linia 4.(tu nic nie ma, bo nie ma takiej linii):", plik.readline())
plik.close()