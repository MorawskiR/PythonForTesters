import pathlib
katalogDomowy=pathlib.Path.home() # Obiekt wskazujący na katalog (*)
katalogBiezacy=pathlib.Path.cwd()
pewienplik=katalogBiezacy / pathlib.Path("witamy.py") # Obiekt wskazujący na plik
print(f"Katalog domowy:{katalogDomowy} \nBieżący katalog:{katalogBiezacy}")
print(f"Nasz pierwszy program w Pythonie: {pewienplik}")
print(f"Dekompozycja składowych - nazwa :{pewienplik.name}")
print(f"Dekompozycja składowych - trzon : {pewienplik.stem}")
print(f"Dekompozycja składowych - suffiks' : {pewienplik.suffix}")
print(f"Dekompozycja składowych - 'parent' : {pewienplik.parent}")
print(f"Dekompozycja składowych - 'anchor' : {pewienplik.anchor}")
katalogBiezacy=pathlib.Path.cwd()
katalogDel=katalogBiezacy / pathlib.Path("testdir2")
try:
    print(f"Chcemy usunać {katalogDel}")
    katalogDel.rmdir() # Usuwamy katalog wskazywany przez obiekt klasy Path (**)
except OSError:
    print("Coś poszło nie tak. Sprawdź, czy katalog istnieje lub\czy nie zawiera plików")