#zad5
lista = []
for liczba in range(1,13):
    lista.append(liczba)
    print(lista)
print("koniec for'a")

#
print("///////////")
#zad6

for element in lista:
    print(element)
#
print("//////////")
#zad7
for element in lista:
    if element%2 ==0:
         print(element)
    else:
        print(element, "nieparzysta")

#zad8

kwadraty = []
for element in lista:
   kwadraty.append(element**2)
print(kwadraty)
#zad9

suma =sum(lista)
print(suma)\

sumalisty = 0
for element in lista:
    print(sumalisty, "+", element, "=", end=" ")
sumalisty += element
print(sumalisty)

#zad10
print(7 in lista)

#inny sposob

#zad11
liczbaEL = len(lista)
srednia = suma/liczbaEL

for element in lista:
    if element > srednia:
