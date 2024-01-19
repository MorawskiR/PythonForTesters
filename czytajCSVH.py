import csv
import pathlib
nazwapliku="seriaH.csv"
plik=pathlib.Path(nazwapliku).open(mode="r", encoding="utf-8", newline='')
CSVreader=csv.DictReader(plik, delimiter=',')
print("Etykiety kolumn wiersza nagłówkowego:", CSVreader.fieldnames) # (*)
print("Wartości w słowniku można adresować, używając etykiet z wiersza nagłówkowego:")
print(f"{CSVreader.fieldnames[0]:10}{CSVreader.fieldnames[1]:11}\{CSVreader.fieldnames[2]:5}{CSVreader.fieldnames[3]:6}\{CSVreader.fieldnames[4]}")
for w in CSVreader:
    print(f"{w['Imię']:10}{w['Nazwisko']:11}{w['Wiek']:5}\{float(w['Płaca']):8.2f}{float(w['Mnożnik premii']):8.2f}")
print("Zawartość odczytanego pliku CSV odczytana jako lista słowników Pythona:")
for w in CSVreader:
    print(w)
plik.close()