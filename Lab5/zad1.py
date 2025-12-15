import random

szczesliwy_numerek = random.randint(1, 25)
print("Szczęśliwy numerek:", szczesliwy_numerek)


#b
import random

roczniki = [2003, 2004, 2005, 2003, 2004, 2002, 2005]
szczesliwy_rocznik = random.choice(roczniki)

print("Roczniki w grupie:", roczniki)
print("Szczęśliwy rocznik:", szczesliwy_rocznik)
#c
import random

liczby = list(range(1, 50))
losowanie = random.sample(liczby, 6)
losowanie.sort()

print("Wylosowane liczby Lotto:", losowanie)
