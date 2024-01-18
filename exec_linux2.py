import subprocess
prog = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True) # (*)
(wynik, err) = prog.communicate() # (**)
print(f"Dziś jest:{wynik}")
prog = subprocess.Popen("who", stdout=subprocess.PIPE, shell=True)
(wynik, err) = prog.communicate()
print(f"\nZalogowani użytkownicy:]n {wynik} ")