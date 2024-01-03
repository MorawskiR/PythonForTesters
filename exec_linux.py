# Stara metoda (obecnie niepolecana)
#import os
#os.system("./bash.sh")
#print("Zewnętrzny program został uruchomiony, wracam do skryptu Pythona")
# Zalecana metoda:
import subprocess
subprocess.call( ['sh', 'bash.sh'] )
print("Zewnętrzny program został uruchomiony, wracam do skryptu Pythona")