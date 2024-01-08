
jezyki = ["C++", "Python", "Java", "Lisp"] #lista

t1=[] #pusta lista
t2=list() # Konstruktor klasy list

if(jezyki[1] == jezyki[-3]):
    print("hello")

print("Metody listy")
print(jezyki[0]) #operator dostepu

#konkatenacja
a=[2, 3]
b=[3,4,5]
print(a+b)

#powielanie operator*
print(a*3)

#sprawdza element na liscie
print("Visual Basic" in jezyki)

print("Metody list")

list = [1,2,3,4,5]

print(list)
list.append(6)
print(list)
list.clear()
list = [1,2,3,4,5]
print(list.count(2))

b=[80,90]
print(list.extend(b))
print(list)
print(list.index(1))
print(list)
list.insert(2,200)
print(list)

a=[10, 20, 30, 40, 8, 60]
print(a.pop(4))

a.remove(10)
print(a)

a.reverse()
print(a)

a.sort()
print(a)