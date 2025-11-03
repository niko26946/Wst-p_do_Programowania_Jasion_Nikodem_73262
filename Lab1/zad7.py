import random

srednie_spalanie = float(input("Podaj średnie spalanie samochodu (l/100 km): "))
droga = random.randint(50, 1000)
zuzycie_paliwa = (srednie_spalanie / 100) * droga
cena_paliwa = 6.5
koszt = zuzycie_paliwa * cena_paliwa

print(f"\nDługość trasy: {droga} km")
print(f"Przewidywane zużycie paliwa: {zuzycie_paliwa:.2f} litrów")
print(f"Szacowany koszt podróży: {koszt:.2f} zł")