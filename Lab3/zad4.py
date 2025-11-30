import random
import string

n = int(input("Podaj liczbę elementów listy (n): "))
x = int(input("Podaj maksymalną długość ciągu znaków (x): "))

lista = []
for _ in range(n):
    dl = random.randint(1, x)
    ciag = ''.join(random.choice(string.ascii_lowercase) for _ in range(dl))
    lista.append(ciag)

print("\nUtworzona lista:", lista)

krotka = tuple(lista)
print("Krotka:", krotka)

ilosc_znakow = sum(len(elem) for elem in krotka)
print("\na) Ilość znaków w krotce:", ilosc_znakow)

ilosc_k = sum(elem.count('k') for elem in krotka)
print("b) Ilość liter 'k':", ilosc_k)

ilosc_kt = sum(elem.count('kt') for elem in krotka)
print("c) Ilość wystąpień 'kt':", ilosc_kt)

s = int(input("\nPodaj wartość s: "))
dluzsze_niz_s = sum(1 for elem in krotka if len(elem) > s)
print("d) Ilość ciągów dłuższych niż", s, ":", dluzsze_niz_s)

