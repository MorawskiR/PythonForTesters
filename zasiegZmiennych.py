v = int() # Pusta deklaracja zmiennej typu int
wynik = 6
print ("wynik=", wynik)
def pi_razy_drzwi(pi, drzwi):
    x=5 #wynik = pi*drzwi (**)
    print("wynik=", wynik)
pi_razy_drzwi(3,4) # Wywołujemy funkcję


def funkcyjka():
    global v
    v=5
    print("Wywołanie lokalne, v=", v)

funkcyjka() # Wywołanie funkcji zmodyfikuje obiekt globalny przypisany do zmiennej v (***)
v=v+1
print("Wywołanie globalne, v=", v)