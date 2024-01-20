import easygui
# msg="Komunikat"
# tytul="Tytuł okna"
# ok_button="nadpisany OK"
# easygui.msgbox(msg, tytul, ok_button)
#
# msg = "Kontynuujemy?"
# title = "Prośba o potwierdzenie"
# pytania =["Tak", "Anuluj" ]
# if easygui.ccbox(msg, title, pytania): # Pierwszy wybór = True
#     pass # Wybrano pierwszy przycisk (OK)
# else: # Wybrano drugi przycisk (Continue)
#     print("Do widzenia!")


# title = "Jaką rasę psów lubisz?"
# pytania=["Jamniki", "Shih-tzu", "Mieszańce"]
# odp=easygui.buttonbox("Wybierz dobrze!", title, pytania, image="tk.gif")
# if odp in pytania:
#     easygui.msgbox("Wybrano" + " " + odp)
# else:
#     easygui.msgbox("Czyżbyś lubił(a) koty?)")


# title = "Scenariusze"
# pytanie = "Wybierz jeden ze scenariuszy do uruchomienia"
# listawyboru=["Test-run1", "Test-run2", "Test-run3", "Test-run4", "Test-run5"]
# odp = easygui.choicebox(pytanie, title, listawyboru, preselect=0)
# easygui.msgbox("Wybrano:"+str(odp))
# # Lista wielokrotego wyboru
# title = "Scenariusze"
# pytanie = "Wybierz jeden lub więcej scenariuszy do uruchomienia"
# listawyboru=["Test-run1", "Test-run2", "Test-run3", "Test-run4", "Test-run5"]
# odp = easygui.multchoicebox(pytanie, title, listawyboru, preselect=0)
# easygui.msgbox("Wybrano:"+str(odp))



msg = "Podaj parametry testu"
title = "Warunki brzegowe"
pola = ["Min", "Max", "Krotność", "Odchyłka"]
wyniki=[]
wyniki = easygui.multenterbox(msg, title, pola)
while 1: # Wymuszamy wprowadzenie każdej z wartości
    if wyniki is None: # Nic nie wybrano
        break
    errmsg = "" # Tworzymy komunikat błędu
    for i in range(len(pola)):
        if wyniki[i].strip() == "":
            errmsg += ('"Pole %s" jest wymagane.\n' % pola[i])
    if errmsg == "":
        break # OK
    wyniki = easygui.multenterbox(errmsg, title, pola, wyniki)
print("Wprowadzono: ", str(wyniki)) # Lista, np. ['10', '20', '5', '0.45']