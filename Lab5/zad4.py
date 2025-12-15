from datetime import datetime, date

# --- USTAW DATY ---
data_laboratoria = date(2025, 12, 15)   # RRRR, MM, DD
data_kolokwium = date(2025, 12, 22)      # RRRR, MM, DD

dzis = date.today()

# obliczenia
dni_od_lab = (dzis - data_laboratoria).days
dni_do_kol = (data_kolokwium - dzis).days

# pl
miesiace = {
    1: "stycznia", 2: "lutego", 3: "marca", 4: "kwietnia",
    5: "maja", 6: "czerwca", 7: "lipca", 8: "sierpnia",
    9: "września", 10: "października", 11: "listopada", 12: "grudnia"
}

# formatowanie dat
lab_txt = f"{data_laboratoria.day} {miesiace[data_laboratoria.month]} {data_laboratoria.year}"
kol_txt = f"{data_kolokwium.day} {miesiace[data_kolokwium.month]} {data_kolokwium.year}"

# wyniki
print(f"Od ostatnich laboratoriów ({lab_txt}) minęło {dni_od_lab} dni.")

if dni_do_kol >= 0:
    print(f"Do kolokwium ({kol_txt}) pozostało {dni_do_kol} dni.")
else:
    print(f"Kolokwium ({kol_txt}) już się odbyło.")
