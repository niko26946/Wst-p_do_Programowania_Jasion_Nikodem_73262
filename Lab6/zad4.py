import pandas as pd

# 1. Utworzenie DataFrame z danymi pracowników
pracownicy = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
})

print("Dane początkowe:")
print(pracownicy)

# a) Pracownicy z pensją > 5000
print("\nPracownicy z pensją > 5000 PLN:")
print(pracownicy[pracownicy['Pensja'] > 5000])

# b) Sortowanie według wieku
print("\nPracownicy posortowani według wieku:")
print(pracownicy.sort_values(by='Wiek'))

# c) Średnia pensja według stanowiska
print("\nŚrednia pensja według stanowiska:")
print(pracownicy.groupby('Stanowisko')['Pensja'].mean())

# d) Zmiana stanowiska i połączenie danych
zmiany = pd.DataFrame({
    'ID': [2, 4],
    'Nowe_stanowisko': ['Senior Programista', 'Team Leader']
})

polaczone = pracownicy.merge(zmiany, on='ID', how='left')

print("\nDane po zmianie stanowiska:")
print(polaczone)

# e) Zapis do pliku CSV
polaczone.to_csv('pracownicy.csv', index=False)

# f) Wczytanie danych z CSV
wczytane = pd.read_csv('pracownicy.csv')

print("\nDane wczytane z pliku CSV:")
print(wczytane)
