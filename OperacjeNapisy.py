sentence = "Palindrome"
print(sentence[0], sentence[1]) #access element

print(sentence[2::5]) # slice

s1 ="Moj pies"
s2="ma na imię Figo"
s3=s1+s2
print(s3)
print(s1*3) # powielanie
print(len(s1)) # len dlugosc napisu

#znaki specjalne
# \t (tabulator), \n (znak nowej linii), \\ (ukośnik pojedynczy
# \), \' (apostrof pojedynczy, zwykły ') oraz \" (pojedynczy cudzysłów prosty ").

#metody klasy STR
sentence1 = "Django"
print(sentence1.center(50)) # Zwraca wyśrodkowany napis do podanej szerokości width, możesz określić też opcjonalny znak wypełniający fillchar inny niż domyślna spacja wypełniająca przestrzeń z lewej i prawej strony.

s="Testerzy lubią Pythona"
print(s.center(30, '*')) # fillchar - znak

str="Testerzy lubią Pythona"
print(str.lower())
print(str.upper())

piesek="Figo"
print(piesek.ljust(20,'*'))
print(piesek.rjust(10,'#'))


s=" Język Python jest fajny"
print(s.lstrip())
print(s.rstrip())

s="***-Język Python jest fajny-***"
print(s.strip('*'))

s="***-Język Python jest fajny-***"
print(s.swapcase())

tytul="Alicja w krainie czaRow"
print(tytul.title())

#analiza
print("ANALIZA ZAWARTOSCI")
s = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
print(s.count("wood"))

print(s.endswith('?'))
print(s.startswith('?'))

s="Testerzy lubią Pythona"
print(s.find("lubią"))

s = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
print(s.find('chuck'))

print("modyfikacje")

s = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
print(s.replace("wood","DREWNO",2))

print(s.split())
print(s.split("if"))

print("ANALIZA SKŁADNIOWA")
s="Kod230"
if s.isalnum():
    print("napis składa się z cyfr i liter alfabetu")

# isalpha()
# isascii()
# isdigit()
# islower()
# isupper()
# isspace()
# istitle()