imie = "Nikodem"
kierunek = "Cyberbezpieczenstwo"
uczelnia = "Wsiz"


# sposób 1
print("Nazywam się")
print(imie)


# sposób 2
print("Nazywam się" + imie)

#sposób 3
print("Nazywam się",imie)

#sposób 4
print(f"Nazywam się  {imie}")

#*
print("Nazywam się", imie, sep="_", end=" ")
print("coś")


print("Nazywam się", imie, "Studiuję kierunek", kierunek, "Na uczelni", uczelnia)