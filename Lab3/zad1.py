imiona = ["Krysztof", "Dawid", "Kamila", "Dominik"]
print(imiona)
for i in imiona:
    print(i)


for i in range(len(imiona)): #iteruje po ideksie
    print(f"index: {i}, imie: {imiona[i]}")


#pod punkt a ver1
print(sorted(imiona))
#ver 2

posortowane_imiona= sorted(imiona)
print(posortowane_imiona)

#podpunkt b

imiona.append("Krysztof")    #dodaje ostatni element
imiona.append("Dawid")
imiona.append("Kamila")
imiona.append("Dominik")
print(imiona)

print(imiona.pop())  #usuwa ostatnie element
print(imiona)

#podpunkt c
imiona.insert(3,"Miłosz")
print(imiona)

#pod punkt d

imiona.reverse()
print(imiona * 2) #jedna lista razy 2