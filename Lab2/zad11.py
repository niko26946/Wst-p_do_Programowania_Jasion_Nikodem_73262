a = int(input("Podaj pierwsza liczbe:"))
b = int(input("Podaj druga liczbe:"))

mniejsza = min(a, b)
wieksza = max(a, b)

x = mniejsza

while x<= wieksza:
    if x % 2!= 0:
        x = x + 1
        continue
    print(x)
    x = x + 1
