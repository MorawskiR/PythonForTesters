# Drukuj wartości od 3 do 4 (wartość 5 jest pomijana!)
for n in range(3, 5):
    print (n, end =" ")
#3 4
# Drukuj wartości od 0 do 4
for n in range(5):
    print (n, end =" ")
#0 1 2 3 4
# Przykład pętli zagnieżdżonej (1)
for p in range(3):
    for q in range(4):
        if q==2:
            print(f"Pomijamy q={q}")
            continue
        print (f"(p={p} q={q})", end =" ")

# Przykład pętli zagnieżdżonej (2)
for p in range(3):
    for q in range(4):
        if q==2:
            print(f"Pomijamy q={q}")
            break
    print (f"(p={p} q={q})", end =" ")


for i in range (0, 100, 10):
    print(i, end= " ")
print("\n")
for i in range (100, 0, -10):
    print(i, end=" ")
print("\n")
for c in "Figo":
    print (c)