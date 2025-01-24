x = int(input())

if x >=1 and x <= 1000:
    for w in range(1,x+1,1):
        if w % 2 == 1:
            print(w)
