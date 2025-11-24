# Program porządkowania trzech liczb bez użycia funkcji sort()

x = float(input("Podaj pierwszą liczbę (x): "))
y = float(input("Podaj drugą liczbę (y): "))
z = float(input("Podaj trzecią liczbę (z): "))

# Zamiana wartości tak, aby ułożyć je rosnąco
if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x

print("Liczby od najmniejszej do największej:")
print(x, y, z)

