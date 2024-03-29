pracownicy = {
"Jan Kowalski":668168555,
"Anna Zwinna":605123001,
"Marek Ekspercki":721003050,
"Jan Bęcki":672000455}
for imie, numer in pracownicy.items(): # Wypisanie zawartości słownika
    print(f"Pracownik: {imie}, telefon:\t{numer}")
print(pracownicy) # Tak też można wypisać zawartość słownika
nazwisko = input("Podaj nazwisko osoby: ") # Sprawdzanie obecności klucza w słowniku:
if nazwisko in pracownicy:
    print(f"Znalazłem {nazwisko} w bazie danych!")
else:
    print(f"Nie znalazłem {nazwisko} w bazie danych!")
# Odczyt danych ze słownika. Przypadek: istnieje para klucz-wartość
print("klucz: Jan Bęcki, wartość: ", pracownicy.get("Jan Bęcki"))
# Odczyt danych ze słownika. Przypadek: NIE istnieje para klucz-wartość
print("klucz: Janek Bęcki, wartość: ", pracownicy.get("Janek Bęcki"))
# Zwraca: None, co z tym fantem robić? W podany niżej sposób możesz uniknąć zwracania pustej
# wartości (None) i wypisać np. „Nie znaleziono wpisu!":
print("klucz: Janek Bęcki, wartość: ", pracownicy.get("Janek Bęcki", "Nie znaleziono wpisu!"))
# Dodanie lub modyfikowanie wpisów w słowniku
print("Rozszerzanie słownika o nowe wpisy (Piotr Wróblewski, tel. 668999550):")
pracownicy["Piotr Wróblewski"]=668999550
print(pracownicy)
print("Aktualizacja zawartości słownika dla wcześniej użytego klucza (Piotr Wróblewski, nowy tel. 668888550 ")
pracownicy["Piotr Wróblewski"]=668888550
print(pracownicy)
# Usunięcie elementu ze słownika
nazwisko = input("Podaj nazwisko osoby do usunięcia: ")
if nazwisko in pracownicy:
    print(f"Znalazłem \'{nazwisko}\' w słowniku, usuwam!!!")
    pracownicy.pop(nazwisko)
else:
    print(f"Nie znalazłem \'{nazwisko}\' w słowniku")
print ("Finalna zawartość listy pracowników:")
print(pracownicy)