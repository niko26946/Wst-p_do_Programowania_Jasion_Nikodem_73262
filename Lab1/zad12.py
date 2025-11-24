# Program obliczania wartości funkcji a(x), b(x) i c(x)

x = float(input("Podaj wartość x: "))

# Funkcja a(x)
if x > 0:
    a = 2 * x
elif x == 0:
    a = 0
else:
    a = -3 * x

# Funkcja b(x)
if x >= 1:
    b = x**2
else:
    b = x

# Funkcja c(x)
if x > 2:
    c = 2 + x
elif x == 2:
    c = 8
else:
    c = x - 4

print("\nWyniki funkcji:")
print("a(x) =", a)
print("b(x) =", b)
print("c(x) =", c)
