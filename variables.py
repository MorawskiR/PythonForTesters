mojKod=0 # Liczba całkowita (typ int)
mojParametr=3.14 # Liczba zmiennopozycyjna (typ float)
wielkaLiczba=4.34561e13 # Notacja 'e': 4.34561 razy 10 do potęgi 13 (typ float)
mojNapis="Napis" # Napis (typ obiektowy str)
mojaLista={"ala", "ma", "kota"} # Zbiór elementów (kolekcja, tutaj typ obiektowy set)
print( mojKod, " --- ", type(mojKod), "\n", # Znak \n wymusza kontynuację w nowej linii
    mojParametr, " --- ", type(mojParametr), "\n",
    mojNapis, " --- ", type(mojNapis), "\n",
    mojaLista, " --- ", type(mojaLista) )
print("Wielka liczba=", wielkaLiczba)