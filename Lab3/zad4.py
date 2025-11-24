import random
n = int(input("Podaj dlugosc listy:"))
z = int(input("Podaj maksymalna dlugosc każdego ze slow:"))
lista = []
for i in range(n):
    d = random.randint(1, x)
    znaki = ["a", "b", "c", "d", "e", "f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    slowo=""
    for j in range(d):
    znak = random.choice(znaki)

    slowo+=znak
    lista.append(slowo)

#print(lista)
krotka =tuple(lista)
print(krotka)
#A
suma_znakow = 0
for slowo in krotka:
    suma_znakow += len(slowo)
print(suma_znakow)
#B
suma_k=0
for slowo in krotka:
    for znak in slowo:
        if znak =="k":
            suma_k += 1

print(suma_k)

#C
suma_kt=0
for slowo in krotka:
    for i in range(len(slowo)-1):
            if slowo[i:i+2] =="kt":
                suma_kt += 1
print(suma_kt)
#D