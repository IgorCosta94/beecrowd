x=int(input())

while x != 0:
    total = 0
    cont = 1
    while cont <= 5:
        if x % 2 == 0:
             total += x
             cont += 1
        x += 1
    print(total)
    x=int(input())

