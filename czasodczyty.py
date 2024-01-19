import time
sekundnik = time.time()
GMT=time.gmtime() # Czas UTC/GMT
Lok=time.localtime() # Czas lokalny
print (f"Liczba sekund od dziejów zarania to {sekundnik}")
print ("Czas bieżący tzw. uniwersalny (UTC albo GMT):\n", GMT)
print(f" Rok {GMT.tm_year}, miesiąc {GMT.tm_mon}, dzień {GMT.tm_mday}")
print(f" Godzina {GMT.tm_hour}, minuta {GMT.tm_min}, sekunda {GMT.tm_sec}")
print(f" Dzień tygodnia (0-6): {GMT.tm_wday}, dzień roku (1-366):\
{GMT.tm_yday}, znacznik DST): {GMT.tm_isdst}") # DST – znacznik czasu letniego}")
print (f"Czas bieżący tzw. uniwersalny (UTC albo GMT):\n{GMT}:")
print ("Czas lokalny:")
print(f" Godzina {Lok.tm_hour}, minuta {Lok.tm_min}, sekunda {Lok.tm_sec}")
print(f" Znacznik czasu letniego: {Lok.tm_isdst}")
print("Funkcja 'ascitime':", time.asctime())

import calendar
cal = calendar.month(2021, 5)
print (cal)

import calendar
cal = calendar.month(2021, 5)
# Częściowa polonizacja wyniku:
print(cal.replace("Mo","Po"))

print ("Kalendarz na rok 2021:")
print ( calendar.calendar(2021) )