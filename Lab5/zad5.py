import keyword

slowa = ["for", "print", "break", "done", "bad"]

for slowo in slowa:
    if keyword.iskeyword(slowo):
        print(f"'{slowo}' jest słowem kluczowym.")
    else:
        print(f"'{slowo}' NIE jest słowem kluczowym.")
