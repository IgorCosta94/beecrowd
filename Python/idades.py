n=int(input())
total=0
cont=0.0
while n > 0:
    total+=n
    cont+=1.0
    n=int(input())
print(f"{total/cont:.2f}")
