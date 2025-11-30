rachunki = {
    "styczeń": 210,
    "luty": 180,
    "marzec": 235,
    "kwiecień": 190,
    "maj": 260
}

wartosci = list(rachunki.values())

maks = max(wartosci)
mini = min(wartosci)
suma = sum(wartosci)
srednia = suma / len(wartosci)

print("Rachunki:", rachunki)
print("Maksymalna wartość:", maks)
print("Minimalna wartość:", mini)
print("Suma:", suma)
print("Średnia:", srednia)

ostatni_miesiac = wartosci[-1]

if ostatni_miesiac > srednia:
    print("Trzeba zacisnąć pasa")
else:
    print("Wszystko okay")

