x=float(input())
n=[0]*100
n[0]=x
print(f"N[0] = {x:.4f}")
for w in range(1,100,1):
    n[w] = n[w-1] / 2
    print(f"N[{w}] = {n[w]:.4f}")
