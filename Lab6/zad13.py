import numpy as np

# 1. Macierz 5x5 wypełniona zerami
macierz = np.zeros((5, 5), dtype=int)

# 2. Ustawienie jedynek na brzegach
macierz[0, :] = 1      # góra
macierz[-1, :] = 1     # dół
macierz[:, 0] = 1      # lewo
macierz[:, -1] = 1     # prawo

print("Macierz początkowa:")
print(macierz)

# 3. Funkcja zamieniająca 0 <-> 1
def zamien_0_1(tablica):
    return 1 - tablica

# 4. Zastosowanie funkcji
odwrocona = zamien_0_1(macierz)

print("\nMacierz po zamianie 0 ↔ 1:")
print(odwrocona)
