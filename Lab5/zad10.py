import random
import math

# pobranie zakresu od użytkownika
a = int(input("Podaj dolny zakres losowania: "))
b = int(input("Podaj górny zakres losowania: "))

# losowanie 10-elementowej krotki
krotka = tuple(random.randint(a, b) for _ in range(10))
print("Wylosowana krotka:", krotka)

# obliczanie średniej geometrycznej
iloczyn = 1
for x in krotka:
    iloczyn *= x

srednia_geometryczna = iloczyn ** (1 / len(krotka))

print("Średnia geometryczna:", srednia_geometryczna)
