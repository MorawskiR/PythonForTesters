print("*** Odczyt pliku GIF w trybie binarnym ***")
plik=open("tk.gif", "rb")
dane = plik.read() # Czytamy cały plik
dlugosc=len(dane)
print("Otwarto plik: ",plik.name)
print("Tryb otwarcia: ",plik.mode)
print("Plik zajmuje", dlugosc, "bajtów na dysku")
plik.seek(0) # Wracamy na początek pliku
print("10 początkowych bajtów:")
for i in range(0,10):
    c=plik.read(1)
    print("Bajt nr:", i, ":", c, "hex:", c.hex())
plik.close()