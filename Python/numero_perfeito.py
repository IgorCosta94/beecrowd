n=int(input())
for a in range(0,n,1):
    x=int(input())
    total = 0
    for b in range(1,x,1):
        if x % b == 0:
            total += b
    if total == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
