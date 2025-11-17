tekst = input("Podaj ciag znakow: ")

odwrocony =""
i = len(tekst) - 1

while i >= 0:
    odwrocony = odwrocony + tekst[i]
    i = i - 1
if tekst == odwrocony:
    print("To jest palindrom")

else:
        print("To nie jest palindrom")
