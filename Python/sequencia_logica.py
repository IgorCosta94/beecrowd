n=int(input())
numero = [1,1,1]
cont = 1  
while cont <= n:
    for x in range(0,2,1):
        if x == 0:
            for w in range(0,3,1):
                if (w == 0):
                    numero[w] = cont
                    print(numero[w],end=" ")
                if(w == 1):
                    numero[w] = pow(numero[0],2)
                    print(numero[w],end=" ")
                if(w == 2):
                    numero[w] = pow(numero[0],3)
                    print(numero[w])
        if x == 1:
            numero[1] = numero[1] + 1
            numero[2] = numero[2] + 1
            for x in range(0,3,1):
                if x != 2:
                    print(numero[x], end=" ")
                if x == 2:
                    print(numero[x])
            cont +=1            
