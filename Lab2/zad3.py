# Program wypisuje n elementow ciagu arytmetycznego

n = int(input("Podaj ile ma byc elementow: "))
a = float(input("Podaj pierwszy wyraz ciagu: "))
r = float(input("Podaj roznice ciagu: "))

print("Elementy ciagu:")

# tutaj obliczam kolejne elementy
i = 0
while i < n:
    element = a + i * r
    print(element)
    i = i + 1
