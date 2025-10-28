droga = float(input("Droga pokonana przez samochów(km):"))
paliwo = float(input("Srednia spalanie (W litrach na 100km):"))

spPaliwo = droga * (droga/100)
cena = 6.5 * spPaliwo

print(f"Spalone paliwo {spPaliwo} ")
print(f"Cena paliwo {cena} ")
