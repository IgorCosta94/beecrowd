n1=int(input())
n2=int(input())
total = 0
if n1 <= n2:
    for w in range(n1,n2+1,1):
        if w % 13 != 0:
            total += w
else:
    for w in range(n2,n1+1,1):
        if w % 13 != 0:
            total += w
print(total)
