n=int(input())
cont = 1
numero=[1,2,3]
while cont <= n:
    for w in range(0,3,1):
        print(numero[w],end=" ")
        numero[w] = numero[w]+4
        if w == 2:
            print("PUM")
    cont +=1
        
