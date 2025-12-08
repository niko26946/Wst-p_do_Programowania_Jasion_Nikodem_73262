def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)

    print("Twoje BMI wynosi:", bmi)

    if bmi < 18.5:
        print("Niedowaga.")
    elif 18.5 <= bmi < 25:
        print("Prawidłowa waga.")
    elif 25 <= bmi < 30:
        print("Nadwaga.")
    else:
        print("Otyłość.")

    return bmi

# przykładowe wywołanie
oblicz_bmi(80, 1.80)
