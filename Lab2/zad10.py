a = int(input("Podaj pierwsza liczbe:"))
b = int(input("Podaj druga liczbe:"))

mniejsza = min(a, b)
wieksza = max(a, b)

x = mniejsza
while x <= wieksza:
    print(x)
    x = x + 1
