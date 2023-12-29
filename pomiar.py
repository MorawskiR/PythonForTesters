import datetime
import math
class Pomiar(object):
    LimitNapiecia=250 # Zmienna klasowa (limit pomiarowy)
    Licznik=0 # Zmienna klasowa (liczba utworzonych obiektów)
    def __init__(self, pAutor, pOdczyt): # Konstruktor
        self._dataczas = str (datetime.datetime.now() )[0:19]
        # Wynik będzie podobny do: 2021-04-20 13:51:27
        self._autor=pAutor
        if math.fabs(pOdczyt) <= Pomiar.LimitNapiecia:
            self._odczyt = pOdczyt
        else:
            raise Exception("Odczyt nie może przekroczyć wartości " + \
                            str(Pomiar.LimitNapiecia) + "V")
        Pomiar.Licznik += 1  # Inkrementacja

        def __str__(self):  # Obiekt jako napis
            return "Odczyt=" + str(self._odczyt) + \
                " Dane kontrolne:|" + self._autor + "|" + self._dataczas

        @property  # Właściwość przeznaczona tylko do odczytu
        def dataczas(self):
            return self._dataczas

        @property  # Jw.
        def autor(self):
            return self._autor

        @property  # Właściwość przeznaczona do odczytu lub modyfikacji
        def odczyt(self):
            return self._odczyt

        @odczyt.setter
        def odczyt(self, korekta):
            if math.fabs(korekta) <= Pomiar.LimitNapiecia:
                self._odczyt = korekta

            else:
                raise Exception("Odczyt nie może przekroczyć wartości " + \
                        str(Pomiar.LimitNapiecia) + "V")

        def komunikat(self):
            print("Cześć, jestem obiektem klasy Pomiar!")

p1=Pomiar("Tester1", 220.1)
print(f"Obiekt 'p1' to [{p1}]")
print("Licznik obiektów:", Pomiar.Licznik)
p2=Pomiar("Tester2", 200)
print(f"Obiekt 'p2' to [{p2}]")
print("Licznik obiektów:", Pomiar.Licznik)
p3=Pomiar("Tester1", -221)
print(f"Obiekt 'p3' to [{p3}]")
print("Licznik obiektów:", Pomiar.Licznik) # Dostęp do atrybutu (*)
# print(f"Obiekt 'p3' utworzył {p3.autor}, data: {p3.dataczas}") # exception works
# print("Modyfikujemy p3 - wartość zmieniona na -230:")
# p3.odczyt=-230 # Wywoła kod funkcji ‘setter’ (**)
# print(f"Obiekt 'p3' to teraz [{p3}]")
# p3.komunikat()