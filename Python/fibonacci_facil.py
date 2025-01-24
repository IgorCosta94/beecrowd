n=int(input())
w=0
x=1
while n < 0 or n > 46:
    n=int(input())

print(w,end=" ")
print(x,end=" ")
for r in range(3,n+1,1):
    y = w + x
    w = x
    x = y
    if r != n:
        print(y,end=" ")
    elif r == n:
        print(y)
