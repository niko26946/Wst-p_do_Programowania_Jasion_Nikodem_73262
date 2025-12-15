import math
import keyword

def pokaz_funkcje(nazwa, obiekt):
    print(f"\nFunkcje w {nazwa}:")
    for element in dir(obiekt):
        try:
            if callable(getattr(obiekt, element)):
                print(element)
        except Exception:
            pass

# math
pokaz_funkcje("module math", math)

# tuple (typ wbudowany)
pokaz_funkcje("type tuple", tuple)

# keyword
pokaz_funkcje("module keyword", keyword)

