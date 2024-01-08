lista_plikow_py=[] # Pusta lista
for s in lista_plikow_all: # Przeszukujemy listę wszystkich plików
    if s.find(".py") != -1: # Znaleziono nazwę pliku z rozszerzeniem .py
        lista_plikow_py.append(s) # Kopiujemy ją do listy lista_plikow_py
print("\nDrukujemy listę plików Pythona (*.py):") # Drukujemy tylko pliki Pythona
print(lista_plikow_py)
lista_plikow_py.sort(reverse=True) # Sortowanie w kierunku wartości malejących
print("\nDrukujemy posortowaną zstępująco listę plików Pythona (*.py):")
print(lista_plikow_py)