class Complex():
# Metoda __init__ to tzw. konstruktor; zostanie wywołana podczas tworzenia obiektu
    def __init__(self, pRe=0, pIm=0): #init constructor
        self.re = pRe  # Tworzymy atrybut Re – część rzeczywista
        self.im = pIm  # Tworzymy atrybut Im – część urojona
        print("Narodził się nowy obiekt... Nie zapomnij o deklaracji 500+")
    def __str__(self):  # Zwróć zawartość obiektu jako napis
        return str(self.re) + "+" + str(self.im) + "*i"
    def dodaj(self, x2):  # Operacja dodawania: x=x+x2
        self.im = self.im + x2.im  # x2 podajemy jako parametr metody dodaj()


n = Complex()
print(f"Obiekt 'n' to [{n}]")  # Sprawdźmy zawartość – metoda wypisze: 0+0*i
x = Complex(5, 8)  # Tworzymy nowy obiekt x = 5 + 8*i
y = Complex(1, 2)  # Tworzymy nowy obiekt y = 1 + 2*i
print(f"Obiekt 'x' to [{x}]")
print(f"Obiekt 'y' to [{y}]")
x.dodaj(y)  # Dodaj do 'x' wartość 'y' (także liczba zespolona)
print(f"Obiekt x=x+y to [{x}]")  # Sprawdźmy aktualną wartość 'x'
# Modyfikujemy pole (możemy to zrobić, bo atrybut jest „publiczny"):
print("Ustawiamy wartość 'Re' obiektu 'x' na -3")
x.re = -3
print(f"Obiekt 'x' to [{x}]")  # Sprawdźmy zawartość 'x'