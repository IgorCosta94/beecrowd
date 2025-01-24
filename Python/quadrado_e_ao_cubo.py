n=int(input())
cont = 1
while cont <= n:
    for w in range(0,3,1):
        if w == 0:
            print(cont,end=" ")
        elif w == 1:
            print(pow(cont,2),end=" ")
        elif w == 2:
            print(pow(cont,3))
    cont +=1
