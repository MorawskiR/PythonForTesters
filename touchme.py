import pathlib
katalogBiezacy=pathlib.Path.cwd() # Obiekt wskazujący na bieżący katalog
# Od tego folderu rozpoczniemy operację "Nieszkodliwy dotyk":
folderStartowy=katalogBiezacy / "test-touch"
if not folderStartowy.exists():
    print(f"Katalog startowy '{folderStartowy}' nie istnieje!")
    exit()
nazwaZnacznika="NasiTuByli.txt"
plikZnacznik=folderStartowy / nazwaZnacznika# Nazwa pliku-znacznika dla folderu startowego
plikZnacznik.touch(exist_ok=True) # Tworzymy pierwszy plik w katalogu startowym
print("Odwiedzam :", folderStartowy.name)
# Przeglądamy zawartość katalogu startowego i jego „potomków”:
for element in folderStartowy.rglob("*"):
    if element.is_dir():
        print("Odwiedzam :", element.name, end= "-->")
        # Tworzę pliki znaczników w podkatalogach
        (element / nazwaZnacznika).touch(exist_ok=True)
        print("Maks i Albert tu byli!")
print()