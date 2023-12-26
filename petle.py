jezyki =["C++", "Python", "Java", "Lisp"] # Prosta lista (tablica napisów)
cyfry = [1, 2, 3, 4, 5, 7, 8, 9, 0]
print("Języki programowania:")
for x in range(len(jezyki)): # Wypisz elementy listy, oddzielając je od siebie spacjami
    print (jezyki[x], end =" ") # end =" " zastępuje ostatni, domyślny znak (\n) dowolnym
# innym (tutaj: spacja)
print() # Przejdź do nowej linii
# Wypisz elementy listy, oddzielając je od siebie spacjami oraz otaczając je nawiasami ():
for x in range(len(cyfry)):
    print (f"({cyfry[x]})", end =" " )
print() # Przejdź do nowej linii
print(*cyfry) # Wypisz zawartość listy 'cyfry', rozdzielając elementy spacjami
# Wypisz zawartość listy 'cyfry', rozdzielając elementy kreskami (-), patrz „sep”
print(*cyfry, sep ="-")

i=1
tmp=0
while i <= 100:
    tmp=tmp+i
    i = i + 1
print("Suma liczb od 1 do 99:", tmp)