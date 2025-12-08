def hanoi(n, start, pomocniczy, cel):
    if n == 1:
        print(f"Przenieś krążek z {start} na {cel}")
    else:
        hanoi(n - 1, start, cel, pomocniczy)
        print(f"Przenieś krążek z {start} na {cel}")
        hanoi(n - 1, pomocniczy, start, cel)

# przykładowe wywołanie
hanoi(3, 'A', 'B', 'C')
