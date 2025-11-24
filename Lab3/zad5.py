lista_zakopow ={"chleb": 7, "maslo":9, "ciastka":10, "pepsi":6,"ser":10, }

print(lista_zakopow)
print(lista_zakopow["chleb"])
print(lista_zakopow.keys())
print(lista_zakopow.values())
print(lista_zakopow.items())

suma = 0
for i in lista_zakopow.values():
    suma+=i
print(suma)

for k, v in lista_zakopow.items():
    print(k,v)