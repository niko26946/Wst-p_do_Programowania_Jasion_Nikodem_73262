import math

def pole_trojkata(a, b, c):
    try:
        # sprawdzenie, czy wszystkie boki są dodatnie
        if a <= 0 or b <= 0 or c <= 0:
            print("Boki muszą być dodatnie.")
            return None

        # sprawdzenie nierówności trójkąta
        if a + b <= c or a + c <= b or b + c <= a:
            print("Z podanych boków nie można utworzyć trójkąta.")
            return None

        # wzór Herona
        s = (a + b + c) / 2
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))

        print("Pole trójkąta wynosi:", pole)
        return pole

    except Exception as e:
        print("Wystąpił błąd:", e)
        return None

# przykładowe wywołanie
pole_trojkata(3, 4, 5)
