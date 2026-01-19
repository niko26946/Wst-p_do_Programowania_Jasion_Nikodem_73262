import numpy as np

# 1. Losowa macierz 5x5
macierz = np.random.randint(0, 100, size=(5, 5))

print("Macierz 5x5:")
print(macierz)

# 2. Największy i najmniejszy element w macierzy
print("\nNajwiększy element:", macierz.max())
print("Najmniejszy element:", macierz.min())

# 3. Największe elementy w każdym wierszu (axis=1)
print("\nNajwiększe elementy w wierszach:")
print(macierz.max(axis=1))

# 4. Największe elementy w każdej kolumnie (axis=0)
print("\nNajwiększe elementy w kolumnach:")
print(macierz.max(axis=0))

# 5. Suma wartości w poszczególnych wierszach
print("\nSuma wartości w wierszach:")
print(macierz.sum(axis=1))
