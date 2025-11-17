#Lb_w = int(input("Podaj liczbę wierszy"))

#for i in range(0,Lb_w):
   #for j in range(Lb_w-(Lb_w-(i+1))):

   #      print("*",end="")   #gwiazdki w jednej lini


  # print("")   #złamanie / podzielenie gwiazdek3





wiersze = int(input("Podaj liczbę wierszy: "))

for i in range(1, wiersze + 1):
    print(" " * (wiersze - i) + "* " * i)


