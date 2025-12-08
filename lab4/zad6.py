def przedstaw_sie(imie, wiek=20):
    print("Imię:", imie)
    print("Wiek:", wiek)

# wyświetlenie opisu funkcji
print(przedstaw_sie.__doc__)

# przykładowe wywołania
przedstaw_sie("Anna", 30)
przedstaw_sie("Kamil")   # tutaj wiek przyjmie wartość domyślną 20
