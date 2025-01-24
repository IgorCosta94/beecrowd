t=int(input())
n=[0]*1000
cont = 0
for w in range(0,1000,1):
    if cont < t:
        n[w] = cont
        print(f"N[{w}] = {cont}")
        cont += 1
    elif cont == t:
        cont = 0
        print(f"N[{w}] = {cont}")
        cont += 1
