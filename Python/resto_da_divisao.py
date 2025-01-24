x=int(input())
y=int(input())

if x <= y:
    for w in range(x+1,y,1):
        if w % 5 == 2 or w % 5 == 3:
            print(w)
elif x >= y:
    for w in range(y+1,x,1):
        if w % 5 == 2 or w % 5 == 3:
            print(w)
