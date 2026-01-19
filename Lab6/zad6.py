import matplotlib.pyplot as plt

# Dane
kategorie = ['Elektronika', 'Odzież', 'Żywność', 'Książki', 'Zabawki']
ilosc_sprzedanych = [120, 200, 150, 80, 60]

# Wykres słupkowy
plt.bar(kategorie, ilosc_sprzedanych)

# Opisy
plt.xlabel('Kategoria produktu')
plt.ylabel('Ilość sprzedanych produktów')
plt.title('Ilość sprzedanych produktów w różnych kategoriach')

# Wyświetlenie wykresu
plt.show()
