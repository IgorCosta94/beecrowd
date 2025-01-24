cont2 = 0
cont = 1
total = 0
while cont != 2:
    n1=float(input())
    if(n1 >= 0.0 and n1<=10):
        cont2 += 1
        total += n1
    else:
        print("nota invalida")
    if cont2 == 2:
        print(f"media = {total/2.0:.2f}")
        cont2 = 0
        total = 0
        cont = int(input("novo calculo (1-sim 2-nao)\n"))
        if cont < 1 or cont > 2:
            while cont < 1 or cont > 2:
                cont = int(input("novo calculo (1-sim 2-nao)\n"))
