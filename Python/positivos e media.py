cont = 0
total = 0
for w in range(1,7,1):
    x = float(input())
    if x > 0:
        cont += 1
        total += x
print(f"{cont} valores positivos")
print(f"{total/cont:.1f}")
