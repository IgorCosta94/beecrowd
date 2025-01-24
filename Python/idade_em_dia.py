aniversario = int(input())

ano = 0
mes = 0
dia = 0

while aniversario > 0:
    if aniversario >= 365:
        ano += 1
        aniversario -= 365
    if aniversario >= 30 and aniversario < 365:
        mes += 1
        aniversario -= 30
    if aniversario > 0 and aniversario <= 29:
        dia += 1
        aniversario -= 1

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
