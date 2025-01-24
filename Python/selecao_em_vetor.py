a=[0]*100
for w in range(0,100,1):
    a[w] = float(input())
    if a[w] <= 10:
        print(f"A[{w}] = {a[w]:.1f}")
