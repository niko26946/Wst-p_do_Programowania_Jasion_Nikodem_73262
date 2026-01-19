import pandas as pd

# 1. Utworzenie DataFrame z danymi studentów (pierwszy termin)
studenci = pd.DataFrame({
    'nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
})

print("Dane studentów – pierwszy termin:")
print(studenci)

# a) Studenci z oceną > 4
print("\nStudenci z oceną > 4:")
print(studenci[studenci['Ocena'] > 4])

# b) Sortowanie według wieku
print("\nStudenci posortowani według wieku:")
print(studenci.sort_values(by='Wiek'))

# c) Średni wiek studentów według ocen
print("\nŚredni wiek według ocen:")
print(studenci.groupby('Ocena')['Wiek'].mean())

# d) Protokół ocen z poprawy (klucz: nr_albumu)
poprawka = pd.DataFrame({
    'nr_albumu': [2, 5],
    'Ocena_poprawka': [4.0, 3.5]
})

polaczone = studenci.merge(poprawka, on='nr_albumu', how='left')

print("\nDane po poprawce:")
print(polaczone)

# e) Zapis do pliku CSV
polaczone.to_csv('studenci.csv', index=False)

# f) Wczytanie danych z CSV
wczytane = pd.read_csv('studenci.csv')

print("\nDane wczytane z pliku CSV:")
print(wczytane)

# g) Dodanie nowego studenta
nowy_student = {
    'nr_albumu': 6,
    'Imię': 'Paweł',
    'Nazwisko': 'Mazur',
    'Ocena': 4.5,
    'Wiek': 22,
    'Ocena_poprawka': None
}

studenci = pd.concat([studenci, pd.DataFrame([nowy_student])], ignore_index=True)

print("\nDane po dodaniu nowego studenta:")
print(studenci)

# h) Unikalne wartości ocen
print("\nUnikalne oceny:")
print(studenci['Ocena'].unique())

# i) Liczba studentów z oceną równą 5
print("\nLiczba studentów z oceną 5:")
print((studenci['Ocena'] == 5).sum())
