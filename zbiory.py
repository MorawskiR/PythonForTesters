zbiornik = {"żaba", "komar", "insekt"}
print ("Zbiór: ", zbiornik)
print ("Spróbujmy dodać do zbiornika kolejną żabę...")
zbiornik.add("żaba")
print ("Aktualny stan zbiornika:")
print ("Zbiór: ", zbiornik)
lista1=[2,3,4,5,6,6,6,9,9,0]
print ("Budowanie zbioru na podstawie listy:", lista1)
print ("Lista 'lista1'=", lista1)
# Alternatywna metoda budowania zbiorów z użyciem konstruktora 'set' załadowanego listą
# elementów:
zbior2=set(lista1)
print ("Zbiór 'zbior2' utworzony z 'lista1'=", zbior2)
print ("Zbiory zawierające elementy różnych typów:")
kodHEX={0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F'}
print ("Dozwolone znaki kodu szesnastkowego:\n", kodHEX)


set1 = {1,2,3,4,5}
set1.add(6)
print(set1)
symbol = set1.pop()

set1.remove(6)
print(set1)
set1.clear()
print(set1)
zb1={5, 6, 7}
zb2={6, 7, 8, 9}
zb3=zb1.union(zb2)
print(zb1|zb2) # Wypisze {5, 6, 7, 8, 9}
print(zb3) # Wypisze {5, 6, 7, 8, 9} – jest to analogiczna operacja
#Jako parametry metody union możesz podać więcej zbiorów, oddzielając