

import os

s = "ala ma kota"
print("user :" , os.getlogin());
print("never late to python")
rok_poprzedni = 2020
print(f"wydanie ksiazki w {rok_poprzedni + 1}")

a=4
b=5 # Źle! Python nie zaakceptuje tej linijki z powodu zastosowanego zbędnego wcięcia
# (nie jest to blok kodu)
if a>5: # Zwróć uwagę na dwukropek po instrukcji warunkowej
    print ("Zmienna a jest większa od 5!")
else:
    print ("Zmienna a jest mniejsza lub równa 5!")