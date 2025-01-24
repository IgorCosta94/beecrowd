n=int(input())
for a in range(0,n,1):
    x=int(input())
    cont = 0
    for b in range(1,x+1,1):
        if x % b == 0:
            cont += 1
    if cont == 2:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
