def ate9(n,n_9):
    print(n_9[n-1])
    print()

def ate14(n,n_9,n_10_90):
    if n > 10 and n < 20:
        print(n_10_90[0]+n_9[n-10-1],end="")
        print()
    elif n == 10:
        print(n_10_90[0])
        print()
    elif n > 20 and n < 30:
        print(n_10_90[1]+n_9[n-20-1],end="")
        print()
    elif n == 20:
        print(n_10_90[1])
        print()
    elif n > 30 and n < 40:
        print(n_10_90[2]+n_9[n-30-1],end="")
        print()
    elif n == 30:
        print(n_10_90[2])
        print()
    elif n > 40 and n < 50:
        print(n_10_90[3]+n_9[n-40-1],end="")
        print()
    elif n == 40:
        print(n_10_90[3])
        print()
    elif n > 50 and n < 60:
        print(n_10_90[4]+n_9[n-50-1],end="")
        print()
    elif n == 50:
        print(n_10_90[4])
        print()
    elif n > 60 and n < 70:
        print(n_10_90[5]+n_9[n-60-1],end="")
        print()
    elif n == 60:
        print(n_10_90[5])
        print()
    elif n > 70 and n < 80:
        print(n_10_90[6]+n_9[n-70-1],end="")
        print()
    elif n == 70:
        print(n_10_90[6])
        print()
    elif n > 80 and n < 90:
        print(n_10_90[7]+n_9[n-80-1],end="")
        print()
    elif n == 80:
        print(n_10_90[7])
        print()
    elif n > 90 and n < 100:
        print(n_10_90[8]+n_9[n-90-1],end="")
        print()
    elif n == 90:
        print(n_10_90[8])
        print()
        
def ate999(n,n_9,n_10_90,n_100_900):
    if n % 100 == 0: 
        print(n_100_900[n // 100 - 1], end="")
        print()
    else:  
        centenas = n // 100
        resto = n % 100
        if resto < 10: 
            print(n_100_900[centenas - 1] + n_9[resto - 1], end="")
            print()
        elif resto % 10 == 0: 
            print(n_100_900[centenas - 1] + n_10_90[resto // 10 - 1], end="")
            print()
        else:  
            print(n_100_900[centenas - 1] + n_10_90[resto // 10 - 1] + n_9[resto % 10-1],end="")
            print()
            
n=int(input())
n_9= ['I','II','III','IV','V','VI','VII','VIII','IX']
n_10_90=['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
n_100_900=['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
if n > 0 and n < 10:
    ate9(n,n_9)
elif n >= 10 and n < 100:
    ate14(n,n_9,n_10_90)
elif n >=100 and n< 1000:
    ate999(n,n_9,n_10_90,n_100_900)
