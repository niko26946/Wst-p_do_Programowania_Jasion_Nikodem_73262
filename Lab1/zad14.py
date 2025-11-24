filename = input("Podaj nazwę pliku: ")

if filename.endswith(".xls") or filename.endswith(".xlsx"):
    print("To jest plik arkusza Excel.")
else:
    print("To NIE jest plik arkusza Excel.")


# Metoda endswith() sprawdza, czy łańcuch znaków kończy się podanym fragmentem.
# Zwraca True jeśli tak, False jeśli nie.
