zdanie=input("Podaj jakieś zdanie:")
print(zdanie)

#Pod punkt a ver z tab a lfabetu
 alfabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
 lb_w =[0,0,0,0,0,0,0]
for znak in zdanie:
    print(f" sprawdzam znak: {znak}")
    for i in range(len(alfabet)):
        print("Czy jest to litera:",alfabet[i])
        if znak == alfabet[i]:
        lb_w.[i]+=1
        print("tak")
        break
#print(lb_w)
print(lista_slow)

for slowo in lista_slow:
    slowo[0].upper()
    slowo[-1].upper()
    print(slowo)


#Tablica ASCIII
