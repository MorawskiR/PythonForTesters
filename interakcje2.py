def wprowadz_liczbe(pytanie, min, max):
    wynik = int()
    napis = pytanie + " od " + str(min) + " do " + str(max)+ " "
    while True:
        try:
            wynik = int(input(napis))
            if wynik not in range(min, max+1):
                print("Błędny zakres!")
                continue
            else:
                break
        except ValueError:
            print ("Ups, to nie jest oczekiwana wartość... Próbuj dalej.")
    return wynik
# Przykład użycia:
x=wprowadz_liczbe("Proszę wprowadzić liczbę",3, 5)
print(x)