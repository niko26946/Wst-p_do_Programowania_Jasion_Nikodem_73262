import matplotlib.pyplot as plt

# Dane
czas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
predkosc = [0, 10, 20, 28, 35, 40, 42, 45, 47, 50]

# Wykres punktowy
plt.scatter(czas, predkosc)

# Opisy osi i tytuł
plt.xlabel('Czas [s]')
plt.ylabel('Prędkość chwilowa [km/h]')
plt.title('Prędkość chwilowa pojazdu w funkcji czasu')

# Wyświetlenie wykresu
plt.show()
