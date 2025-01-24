n=int(input())
cont = 1

while cont <= n:
    x=int(input())
    y=int(input())

    if  y == 0:
        print("Divisão impossivel")
    else:
        print(f"{((x*1.0) / y):.1f}")
    cont += 1
