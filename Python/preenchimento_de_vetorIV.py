par = [0]*5
impar = [0] *5
cont_p = 0
cont_i = 0
for w in range(0,15,1):
    n=int(input())
    a=abs(n)
    if a % 2 == 0:
        par[cont_p] = n
        cont_p += 1 
    elif a % 2 == 1:
        impar[cont_i] = n
        cont_i += 1
        
    if cont_p == 5:
        for e in range(0,len(par),1):
            print(f"par[{e}] = {par[e]}")
        par = [0]*5
        cont_p = 0
    elif cont_i == 5:
        for g in range(0,len(impar),1):
            print(f"impar[{g}] = {impar[g]}")
        impar = [0]*5
        cont_i = 0
        
for w in range(0,len(impar),1):
    if impar[w] != 0:
        print(f"impar[{w}] = {impar[w]}")
        
for w in range(0,len(par),1):
    if par[w] != 0:
        print(f"par[{w}] = {par[w]}")    
        
