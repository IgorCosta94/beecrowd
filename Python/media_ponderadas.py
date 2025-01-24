n = int(input())

cont = 1
cont2 = 0
total = 0
total2 = 0

peso = [2,3,5]

while cont <= n:
    x = float(input())
    total += (x * peso[cont2])
    print(peso[cont2])
    total2 += x
    cont2 += 1
    if cont2 == 3:
        print(total/total2)
        cont += 1
        cont2 = 0



        
        
