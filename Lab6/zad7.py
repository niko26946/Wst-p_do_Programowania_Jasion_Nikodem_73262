import matplotlib.pyplot as plt

kategorie = ['Elektronika', 'Odzież', 'Spożywcze', 'Meble', 'Inne']
sprzedaz = [35, 25, 20, 10, 10]  # wartości procentowe

# Wykres
plt.figure(figsize=(10, 10))
plt.pie(
    sprzedaz,
    labels=kategorie,
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Procentowy udział kategorii w całkowitej sprzedaży')
plt.axis('equal')  # koło zamiast elipsy

plt.show()
