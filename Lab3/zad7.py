import random

a = random.randint(3, 7)
b = random.randint(3, 7)

X = {random.randint(0, 10) for _ in range(a)}
Y = {random.randint(0, 10) for _ in range(b)}

print("X =", X)
print("Y =", Y)

print("Czy X zawiera 5?", 5 in X)
print("Czy X jest podzbiorem Y?", X.issubset(Y))
print("Czy Y jest podzbiorem X?", Y.issubset(X))

print("Suma zbiorów:", X | Y)
print("Różnica X - Y:", X - Y)
print("Różnica Y - X:", Y - X)
print("Iloczyn:", X & Y)

print("Najwyższy element w obu zbiorach:", max(X | Y))

if X:
    pierwszy = next(iter(X))
    X.remove(pierwszy)
    Y.add(pierwszy)

print("Po przeniesieniu elementu z X do Y:")
print("X =", X)
print("Y =", Y)

Y.update(X)
print("Po skopiowaniu elementów X do Y:")
print("X =", X)
print("Y =", Y)

X.clear()
Y.clear()

print("Po wyczyszczeniu:")
print("X =", X)
print("Y =", Y)
