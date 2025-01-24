n= int(input())

while n <=0 or n >=15:
    n= int(input())
while n != 0:
    m=[[1]*n]*n
    for w in range(0,n,1):
        if w >= 1:
            m[w][0] = m[w-1][0] * 2
        for x in range(0,n,1):
            if x >= 1:
                m[w][x] = m[w][x-1] * 2
            if n <= 2:
                t=1
            elif n > 2 and n <= 4:
                t=2
            elif n  == 5:
                t=3
            elif n > 5 and n <=7:
                t=4
            elif n > 7 and n <=9:
                t=5
            elif n == 10:
                t=6
            elif n > 10 and n <= 12:
                t = 7
            elif n > 12 and n <= 14:
                t = 8
            elif n == 15:
                t=9
            if x < n-1:
                print(f"{m[w][x]:>{t}}",end=" ")
            elif x == n-1:
                print(f"{m[w][x]:>{t}}")
    print()
    n= int(input())
    while n <=0 or n >=15:
        n= int(input())
