x=int(input())
z=int(input())
soma = x
cont = 1
while z <= x:
    z=int(input())

while x < z:
    soma += 1
    x += soma
    cont += 1

print(cont)
