wiek = int(input("Ile masz lat:"))

if (wiek >0) and (wiek < 150):
    #wycena biletów
    if wiek <4:
        print("Wchodzi za darmo")
    elif wiek <18:
        print("Cena biletu to 10zł")
    else:
        student = input("Czy studiuje? (Tak/Nie) ")
        if student == "Tak":
            print("Cena biletu to 15zł")
        else:
            print("Cena biletu to 20zł")



else:
    print("Nieprawidłowe dane")


