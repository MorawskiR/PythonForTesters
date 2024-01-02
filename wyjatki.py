while True:
    try:
        x = int(input("Proszę wprowadzić liczbę:"))
        break
    except ValueError:
        print ("Ups, to raczej nie jest liczba... Próbuj dalej.")
    finally:
        print("dupa")
print (f"Brawo, na to czekałem! Wprowadzono liczbę: {x}") # (*)

