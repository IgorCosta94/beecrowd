m=int(input())
n=int(input())
total = 0 
while m > 0 and n > 0:

    if n < m:
        for w in range(n,m+1,1):
            print(w,end=" ")
            total += w
        print("Sum=",total)
    elif m < n:
        for w in range(m,n+1,1):
            print(w,end=" ")
            total += w
        print("Sum=",total)
        
    total=0
    m=int(input())
    n=int(input())
