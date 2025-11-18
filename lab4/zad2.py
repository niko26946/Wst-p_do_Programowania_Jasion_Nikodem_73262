def pole_trapezu(a,b,h):
    if (a >=0) and (b>=0) and (h>=0):
        return ((a+b))*h)/2
    else:
        return None

print(pole_trapezu(