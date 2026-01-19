import numpy as np

# 1. Losowa macierz 5x5
macierz = np.random.randint(0, 50, size=(5, 5))

print("Macierz 5x5:")
print(macierz)

# 2. Elementy większe niż 20
wieksze_niz_20 = macierz > 20

print("\nElementy większe niż 20:")
print(macierz[wieksze_niz_20])

# Liczba elementów > 20
print("Liczba elementów > 20:", np.sum(wieksze_niz_20))

# 3. Średnia całej tablicy
print("Średnia wartości w tablicy:", macierz.mean())
