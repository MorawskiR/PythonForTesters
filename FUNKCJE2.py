def scenariusz_testowy(**params):
    t1=params["timing1"]
    t2=params["timing2"]
    s=params["napis"]
    print(f" timing1={t1}, timing2={t2}, napis={s}")
# Testujemy wywołanie funkcji scenariusz_testowy:
scenariusz_testowy(timing1=50, timing2=100, napis="ala")
#scenariusz_testowy(timing5=50, timing2=100, napis="ala") # Błąd, patrz 'timing5

