x = int(input())
cont = 1
dentro = 0
fora = 0
if x < 10000:
    while cont <= x:
        numero = int(input())
        if numero > pow(-10,7) and numero < pow(10,7):
            if numero >= 10 and numero <= 20:
                dentro += 1
            else:
                fora += 1
        cont += 1
print(f"{dentro} in")
print(f"{fora} out")
