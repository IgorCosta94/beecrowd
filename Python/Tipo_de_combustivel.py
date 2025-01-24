tipo = int(input())

cont_alcool = 0
cont_gasolina = 0
cont_diesel = 0

while tipo < 1 or tipo > 4:
    tipo = int(input())

while tipo != 4:
    if tipo == 1:
        cont_alcool += 1
    elif tipo == 2:
        cont_gasolina += 1
    elif tipo == 3:
        cont_diesel += 1
        
    tipo = int(input())
    while tipo < 1 or tipo > 4:
        tipo = int(input())

print("MUITO OBRIGADO")
print(f"Alcool: {cont_alcool}")
print(f"Gasolina: {cont_gasolina}")
print(f"Diesel: {cont_diesel}")
