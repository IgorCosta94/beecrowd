x=[0,0,0,0,0,0,0,0,0,0]
for w in range(0,10,1):
    n=int(input())
    if n <= 0:
        x[w] = 1
    elif n > 0:
        x[w] = n
    print(f"X[{w}] = {x[w]}")

