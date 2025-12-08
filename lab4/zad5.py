def srednia(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# przykładowe wywołanie
dane = [4, 7, 2, 10]
wynik = srednia(dane)
print("Średnia wynosi:", wynik)
