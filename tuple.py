tupla1 = (1, 1, 2, 3, 5, 8, 13)  # Najpopularniejsza notacja
print(len(tupla1))  # Wypisze 7, tj. długość tupli
#tupla1[3] = 100  # Błąd, tupli nie można modyfikować! (*)

# Alternatywna notacja, z użyciem konstruktora klasy tuple:
tupla2=tuple ( (1, 1, 2, 3, 5, 8, 13) )
tupla3=("Dr Who", "Dawid Tennant", 10) # Patrz uwaga (**)
tupla4=("Dr Who", "Jodie Whittaker", 13)
tupla3_plus_tupla4=tupla3+tupla4
print(tupla4) # Wypisze: (' Dr Who', 'Jodie Whittaker', 13)
print(tupla3_plus_tupla4)
# Wypisze: ('Dr Who', 'Dawid Tennant', 10, 'Dr Who', 'Jodie Whittaker', 13)
print(tupla4[1]) # Wypisze: Jodie Whittaker

print("Ilustracja niebezpośredniego modyfikowania zawartości tupli")
nazwy_skrocone=['pon', 'wt', 'śr', 'czw', 'pt', 'sob'] # Ups, na tej liście brakuje niedzieli!
tupla5=("dni", nazwy_skrocone)
print("Tupla oryginalna, dwuelementowa:", tupla5)
# Modyfikujemy zawartość listy nazwy_skrocone (sama tupla5 jest nienaruszona)
tupla5[1].append("nd") # Dodajemy element na koniec listy nazwy_skrocone
print("Tupla po dodaniu 'nd' do listy wskazywanej przez drugi element tupli:\n", tupla5)

print("Modyfikacja tupli przez konwersję na listę")
dni_robocze=('pon', 'wt', 'śr', 'czw', 'pt')
print("Dni robocze", dni_robocze) # Wypisze: Dni robocze ('pon', 'wt', 'śr', 'czw', 'pt')
dni_robocze_lista=list(dni_robocze) # Tworzymy listę na podstawie tupli
dni_robocze_lista.append('sob') # Dodajemy 'sob' do listy
dni_robocze=tuple(dni_robocze_lista) # Tworzymy tuplę na podstawie listy
print("Dni robocze", dni_robocze) # Wypisze: Dni robocze ('pon', 'wt', 'śr', 'czw', 'pt', 'sob')


dozwolone_waluty=('PLN', 'EUR', 'USD') # Tupla
print ("Dozwolone waluty to:", dozwolone_waluty)
s=input("Podaj walutę: ") # Program poprosi użytkownika o wpisanie danych
if s in dozwolone_waluty:
    print("Poprawna waluta")
else:
    print("Nieznany kod waluty")