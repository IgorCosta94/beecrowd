total = 0
x=1.0
for s in range(1,40,2):
    total +=s/x
    x *= 2
print(f"{total:.2f}")
