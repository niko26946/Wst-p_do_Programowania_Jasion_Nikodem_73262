def opcja_a():
    imie = input("Podaj imię: ")
    print("Witaj", imie)



def opcja_b():
    wiek = input("Podaj swój wiek: ")
    print("Twój wiek to:", wiek)


def opcja_c():
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    inicjaly = imie[0].upper() + nazwisko[0].upper()
    print("Twoje inicjały to:", inicjaly)


def opcja_d():
    tekst = input("Podaj łańcuch znaków: ")
    for _ in range(5):
        print(tekst)


def opcja_e():
    a = input("Podaj pierwszy łańcuch: ")
    b = input("Podaj drugi łańcuch: ")
    c = a + b
    print("Połączony łańcuch:", c)


def opcja_f():
    a = input("Podaj pierwszy łańcuch: ")
    b = input("Podaj drugi łańcuch: ")

    polowa_a = len(a) // 2
    polowa_b = len(b) // 2

    c = a[:polowa_a] + b[polowa_b:]
    print("Nowy łańcuch:", c)


while True:
    print("\n--- MENU ---")
    print("a) Wczytaj imię i wyświetl powitanie")
    print("b) Wczytaj wiek i wyświetl")
    print("c) Wyświetl inicjały")
    print("d) 5x wyświetl łańcuch")
    print("e) Połącz dwa łańcuchy")
    print("f) Połącz połowy dwóch łańcuchów")
    print("q) Zakończ program")

    wybor = input("Wybierz opcję: ")

    if wybor == "a":
        opcja_a()
    elif wybor == "b":
        opcja_b()
    elif wybor == "c":
        opcja_c()
    elif wybor == "d":
        opcja_d()
    elif wybor == "e":
        opcja_e()
    elif wybor == "f":
        opcja_f()
    elif wybor == "q":
        print("Koniec programu.")
        break
    else:
        print("Nie ma takiej opcji!")
