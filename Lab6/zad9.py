import matplotlib.pyplot as plt

# Dane – oceny studentów
oceny = [4.5, 3.0, 5.0, 4.0, 2.5, 4.5, 5.0, 3.5]

# Histogram
plt.hist(oceny, bins=5)

# Opisy
plt.xlabel('Ocena')
plt.ylabel('Liczba studentów')
plt.title('Rozkład ocen studentów')

# Wyświetlenie wykresu
plt.show()
