s = "Alicja w krainie czarów" # Tworzymy nowy obiekt klasy str (zwykły napis)
liczba="14" # Tworzymy nowy obiekt klasy str (ciąg znaków zawierający liczbę)
print ("Ciąg \"14\" to liczba?", liczba.isdigit())
print( s.upper() ) # Metoda upper() zwraca napis zawierający wszystkie duże litery
print( s.lower() ) # Metoda lower() zwraca napis zawierający wszystkie małe litery
# Metoda swapcase() zwraca napis, w którym zamieniono duże litery na małe i odwrotnie:
print( s.swapcase() )
tytul= "\n\t\t** Nowy wspaniały Świat **\n"
print("Tytuł:", tytul, len(tytul))
# strip() — patrz „Napisy w Pythonie”
print("Tytuł po użyciu strip():", tytul.strip(), len(tytul.strip()) )
x = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
print(x)
print("Podmieniamy słowo 'wood' na 'drewno':")
print(x.replace("wood", "drewno") )