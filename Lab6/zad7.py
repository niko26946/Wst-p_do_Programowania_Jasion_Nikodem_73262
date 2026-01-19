import matplotlib.pyplot as plt

# Dane
kategorie = ['Elektronika', 'Odzież', 'Żywność', 'Książki', 'Zabawki']
sprzedaz = [120, 200, 150, 80, 60]

# Wykres kołowy
plt.pie(sprzedaz, labels=kategorie, autopct='%1.1f%%', startangle=90)

# Tytuł
plt.title('Procentowy udział kategorii w całkowitej sprzedaży')

# Zachowanie koła (a nie elipsy)
plt.axis('equal')

# Wyświetlenie wykresu
plt.show()
