import pandas as pd
# W systemie Windows użyj następującego formatu ścieżki: r"misiePanda\<nazwa pliku>.csv"
pomiary = pd.read_csv("dane1.csv")
pomiary.dropna(inplace=True) # Kasujemy wiersze zawierające puste komórki (NaN)
print("Zaimportowane typy danych:\n", pomiary.dtypes)
print("Zaimportowana tabela:\n", pomiary)

print("Dodaję kolumnę 'Pomiar OK?' i wypełniam ją wartością 'False':")
pomiary["Pomiar OK?"]=False

print("Zaimportowana tabela:\n", pomiary)