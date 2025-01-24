print("dia",end=" ")

dia = int(input())
horas = int(input())
minutos = int(input())
segundos = int(input())

horas = horas * 3600
minutos = minutos * 60
total = horas + minutos +segundos

print("dia",end=" ")

diat = int(input())
horast = int(input())
minutost = int(input())
segundost = int(input())

diat = (diat - dia) *86400

horast = horast * 3600
minutost = minutost * 60
total2=horast+minutost + segundost

tempo = diat - (total - total2)

if tempo >= 60:
    segundos = 0
    minutos = 0
    horas = 0
    dia = 0
    x = 0

    while tempo >= 0:
        if x < 60 and tempo < 60:
            segundos = x
        if x == 60 and tempo < 3600:
            minutos +=1
            x = 0
        if tempo >= 3600:
            horas += 1
            tempo -= 3600
        if tempo >= 86400:
            dia += 1
            tempo -= 86400

        tempo -= 1
        x +=1

    print(f"{dia} dia(s)")
    print(f"{horas} horas(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")
