print("=== KALKULATOR ===")
x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj drugą liczbę: "))

print("Wybierz działanie:")
print("+   dodawanie")
print("-   odejmowanie")
print("*   mnożenie")
print("/   dzielenie")

op = input("Podaj symbol działania: ")

if op == "+":
    wynik = x + y
elif op == "-":
    wynik = x - y
elif op == "*":
    wynik = x * y
elif op == "/":
    if y == 0:
        wynik = "Błąd: nie można dzielić przez zero!"
    else:
        wynik = x / y
else:
    wynik = "Nieznany operator!"

print("Wynik:", wynik)
