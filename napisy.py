s1="Alicja "# Pierwszy napis (s1)
s2=" w krainie czarów" # Drugi napis (s2)
s3=s1.rstrip()+s2 # Metoda rstrip() usuwa spacje z prawej strony napisu s1
print(s3) # Program wypisze ciąg znaków „Alicja w krainie czarów” (bez apostrofów)

s=" * Firma 'Big Deal S.A.' – wyniki roczne * "
print(s) # Wypisze: " * Firma 'Big Deal S.A.' – wyniki roczne * " (bez cudzysłowów)

komunikat=" Strefa wolna od zbędnej teorii" # Zmienna tekstowa
jezyki = ["C++", "Python", "Java", "Lisp"] # Prosta lista (lub klasycznie: tablica)
print("Komunikat:", komunikat)
print("Długość powyższego napisu”", len(komunikat))
print("*--------------------------------------------*")
print("*\t\tNapis po podwójnym '\t' (tabulator)*")
print(f"'The Zen of Python' można przetłumaczyć jako:\n\n{jezyki[1]} jest łatwy \
do nauki") # (*)
print( "'The Zen of Python' można przetłumaczyć jako:\n\n" + jezyki[1] +" jest\
łatwy do nauki") # (**)

print(3*"Alicja w krainie czarów")

print("Alicja w krainie czarów" \
+ " - " \
+"Alicja po drugiej stronie lustra")