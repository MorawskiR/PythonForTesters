mojNapis="Napis" # Zmienna tekstowa (*)
mojNapis2=mojNapis
print("mojNapis =", mojNapis)
print("mojNapis2=", mojNapis2)
print("adres mojNapis=", id(mojNapis))
print("adres mojNapis2", id(mojNapis2))
# Patrz opis operatora 'is' w książce
print ("Wynik porównania 'mojNapis is MojNapis2': ", mojNapis is mojNapis2)
mojNapis2=mojNapis[0]+mojNapis2 # Tworzymy nowy obiekt zawierający ciąg 'NNapis' (**)
print("mojNapis =", mojNapis) # Wypisze: mojNapis = Napis
print("mojNapis2=", mojNapis2) # Wypisze: mojNapis2 = NNapis
print("adres mojNapis= ", id(mojNapis)) # "Stary" obiekt, utworzony w linii (*)
print("adres mojNapis2=", id(mojNapis2)) # "Nowy" obiekt, utworzony w linii (**)