n=int(input())
cont2 = 1
while cont2 <= 2:
    x=int(input())
    y=int(input())
    total = 0
    cont = 1
    while cont <= y:
        if x % 2 == 1:
            total += x
            cont += 1
        x += 1
        
    print(total)
    cont2 += 1

