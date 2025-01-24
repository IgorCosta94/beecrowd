tempo = int(input())

segundos = 0
minutos = 0
horas = 0
x = 0

while tempo >= 0:
    if x < 60 and tempo < 60:
        segundos = x
    elif x == 60 and tempo < 3600:
        minutos +=1
        x = 0
    elif tempo >= 3600:
        horas += 1
        tempo -= 3600

    tempo -= 1
    x +=1

print(f"{horas}:{minutos}:{segundos}")
