import matplotlib.pyplot as plt

czas = [0, 1, 2, 3, 4, 5, 6]
predkosc = [0, 5, 12, 18, 20, 22, 25]

#Wykres punktowy
plt.scatter(czas, predkosc, color='yellow')

plt.xlabel('Czas [s]')
plt.ylabel('Prędkość chwilowa [m/s]')

plt.title('Prędkość chwilowa pojazdu w funkcji czasu')

#Siatka
plt.grid(True)

plt.show()
