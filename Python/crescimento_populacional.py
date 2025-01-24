t=int(input())
cont2= 1   
while cont2<=t:
    cont = 1
    pa=int(input())
    pb=int(input())
    g1=float(input())
    g2=float(input())
    
    pa = pa + int((pa * (g1/100)))
    if g2 == 0:
        pb = pb
        while pa <= pb and cont <= 100:
            pa += int((pa * (g1/100)))
            cont+=1
    if g2 > 0:
        pb = pb + int(pb * (g2/100))
        while pa <= pb and cont <= 100:
            pa += int(pa * (g1/100))
            pb += int(pb * (g2/100))
            cont+=1
    if cont > 100:
        print("Mais de 1 seculo.")
        break
    else:
        print(f"{cont} anos.")
    cont2+=1
