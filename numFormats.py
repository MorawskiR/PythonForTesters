#Ustalamy szerokość na 6 znaków (ograniczniki >
#oraz < są dodane sztucznie, aby ułatwić analizę):

x=23
print(f">{x:6}<") # Wynik: > 23<

x=23.346
print(f"{x:.2f}") # Wynik: 23.35
print(f"{x:.4f}") # Wynik: 23.3460


x=23.346
print(f">{x:8.2f}<") # Wynik: > 23.35< Ustalamy szerokość na 8 znaków i 2 znaki po przecinku:

x=23.346
print(f">{x:<8.2f}<") # Wynik: >23.35 < < Wyrównanie zawartości do lewej strony w ramach dostępnej lub ustalonej szerokości pola.

x=23
print(f">{x:^8}<") # Wynik: > 23 <

x=-23.346
print(f">{x:=8.2f}<") # Wynik: >- 23.35<

x=23.346
print(f">{x:+8.2f}<") # Wynik: > +23.35<

x=234001343.23
print(f">{x:,}<") # Wynik: >234,001,343.23<


z=65345
print(f"{z:b}") # Wynik: 1111111101000001

z=65345
print(f"{z:o}") # Wynik: 177501

z=65345
print(f"{z:x}") # Wynik: ff41

h=0x1f
print(f"{h:d}") # Wynik: 31

a=2.5888
b=0.23
print(f"{a:.1%}") # Wynik: 258.9%
print(f"{b:.0%}") # Wynik: 23% # % Prezentacja ułamka w formacie procentowym

a=2588.92
print(f"{a:e}") # Wynik: 2.588920e+03 e Liczba w systemie „naukowym” (tzw. notacja wykładnicza opisywana jako a·10n, na ekranie wyświetlana w formacie ae+n, w której a mnożymy przez 10n.