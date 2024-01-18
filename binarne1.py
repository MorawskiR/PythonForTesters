# Moduł picle umożliwia tzw. serializację obiektów Pythona i ich zapis do pliku dyskowego
import pickle
pracownicy = { # Słownik Pythona z kilkoma wpisami
    "Jan Kowalski":668168555,
    "Anna Zwinna":605123001,
    "Marek Ekspercki":721003050}
print("Lista Pythona:", pracownicy) # Sprawdzamy zawartość
plik_out=open("binarne1.bin", "wb") # W tym pliku zapiszemy obiekt Pythona
pickle.dump(pracownicy, plik_out)
plik_out.close() # (*)
del pracownicy # Usuwamy obiekt z pamięci komputera
input("Zapisano do pliku, naciśnij Enter, aby sprawdzić wynik operacji:")
plik_in=open("binarne1.bin", "rb") # Sprawdzamy wynik
pracownicy_z_dysku = None # Pusta (na razie) zmienna
pracownicy_z_dysku = pickle.load(plik_in) # Ładujemy zawartość nowej zmiennej
print("Słownik odczytany z dysku:") # danymi odczytanymi z dysku
print(pracownicy_z_dysku)
plik_in.close()