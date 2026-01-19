import numpy as np

# 1. Lista potęg liczby 2
lista_wagi = [128, 64, 32, 16, 8, 4, 2, 1]

# 2. Tablica ndarray z wagami
wagi = np.array(lista_wagi)

# 3. Losowa tablica binarna (0 i 1)
liczba_bin = np.random.randint(0, 2, size=8)

print("Wagi:", wagi)
print("Liczba binarna:", liczba_bin)

# 4. Funkcja obliczająca wartość liczby binarnej
def wartosc_liczby_bin(wagi, liczba_bin):
    return np.sum(wagi * liczba_bin)

# 5. Obliczenie wartości dziesiętnej
wartosc = wartosc_liczby_bin(wagi, liczba_bin)

print("Wartość liczby dziesiętnej:", wartosc)
