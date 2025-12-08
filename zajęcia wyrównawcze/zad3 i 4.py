lista = ["kot", "pies", "koń"] #zad 3 i 4

#ostatni: ideks dosłowny
liczbaElementow = len(lista)
print(liczbaElementow)
indexostatniego = liczbaElementow - 1
print(indexostatniego)
print(lista[indexostatniego])

#ideks uprosczony
print(lista[-1])

#ostatni :ze zmiana zawartosci listy (usunięcie elementu)

print(lista.pop())
print(lista)