import math

print("Rozwiązywanie równania ax^2 + bx + c = 0")

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a == 0:
    print("To nie jest równanie kwadratowe (a = 0).")
else:
    delta = b**2 - 4*a*c
    print("Delta =", delta)

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print("Dwa rozwiązania:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Jedno rozwiązanie:")
        print("x =", x)
    else:
        print("Brak rozwiązań rzeczywistych (delta < 0).")
