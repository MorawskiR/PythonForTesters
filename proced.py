def poleKola(r):
    return 3.14*r*r

komunikat = "[Odmówił podania]"
def pacjent(numer, imie=komunikat, nazwisko=komunikat): # (*)
    print(f"Pacjent: nr={numer} imię: {imie} nazwisko: {nazwisko}")
# Testujemy wywołanie funkcji pacjent:
pacjent(4)
pacjent(5, "Jan", "Kowalski")

# Przykład funkcji rekurencyjnej z jednym parametrem:
def silnia(n):
    if n == 0:
        return 1 # (**)
    else:
        return n * silnia(n - 1)
print("silnia(5)=", silnia(5)) # Testujemy funkcję silnia()

def parametry(*params):
    for x in range(0, len(params) ): # Funkcja len() zwróci liczbę przekazanych parametrów
        print(f"Parametr {x} to {params[x]} ") # Wypisz każdy parametr
# Testujemy wywołanie funkcji parametry:
parametry(2, "New York", 6, 6.5)