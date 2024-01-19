import datetime
print("Odczyt daty i czasu w formacie napisu")
s=str(datetime.datetime.now())
print (f" Czas i data bieżące - format pełny {s}")
print (f" Czas i data bieżące - wersja skrócona {s[0:16]}") # (*)
print("Odczyt daty - dekompozycja składowych")
dzis=str( datetime.date.today() )
print(" Wydruk w formie tekstowej:", dzis)
dzis_rozszerz= datetime.datetime.strptime(dzis, "%Y-%m-%d") # (**)
print(f" Dzień: {dzis_rozszerz.day}, miesiąc: {dzis_rozszerz.month}, rok:{dzis_rozszerz.year}")
print("Odczyt daty i czasu - dekompozycja składowych")
teraz = datetime.datetime.now()
print(f" Data -> Dzień: {teraz.day}, miesiąc: {teraz.month}, rok: {teraz.year}")
print(f" Czas -> Godzina: {teraz.hour}, minuta: {teraz.minute}, sekunda: {teraz.second}")

print("-------------------------------")
import datetime
t = datetime.datetime.now()
print(t.strftime("%Y-%m-%d %H:%M:%S")) # 2021-05-05 20:20:15
print(t.strftime("%d/%m/%Y Nr tygodnia: %U")) # 05/05/2021 Nr tygodnia: 18
print(t.strftime("%Y\\%m\\%d")) # 2021\05\05
print(t.strftime("%I:%M:%S %p")) # 08:20:15 PM
print(t.strftime("%A - %b %d, %Y")) # Wednesday – May 05, 2021