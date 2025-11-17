zdanie = input("Podaj zdanie: ")

# a)
litery = []
for z in zdanie.lower():
    if z >= "a" and z <= "z":
        if z not in litery:
            litery.append(z)

litery.sort()
print("Litery w zdaniu:", litery)

alfabet = list("abcdefghijklmnopqrstuvwxyz")
brak = []
for l in alfabet:
    if l not in litery:
        brak.append(l)

print("Brakujace litery:", brak)

# b)
lista_b = list(zdanie)
wynik_b = []
i = 0
while i < len(lista_b):
    if i % 2 == 0:
        wynik_b.append(lista_b[i])
    i = i + 1
print("Po usunieciu nieparzystych:", "".join(wynik_b))

# c)
wyrazy = zdanie.split()
nowe = []
for w in wyrazy:
    if len(w) > 1:
        w = w[0].upper() + w[1:-1] + w[-1].upper()
    else:
        w = w.upper()
    nowe.append(w)
print("Wyrazy z wielkimi poczatkiem i koncem:", " ".join(nowe))

# d)
wyrazy2 = zdanie.split()
naj = ""
for w in wyrazy2:
    if len(w) > len(naj):
        naj = w
print("Najdluzsze slowo:", naj)
print("Dlugosc:", len(naj))

# e)
lista_e = list(zdanie)
zrobione = []
wynik_e = []
for z in lista_e:
    if z in zrobione:
        wynik_e.append("@")
    else:
        wynik_e.append(z)
        zrobione.append(z)
print("Powtorzenia zamienione na @:", "".join(wynik_e))
