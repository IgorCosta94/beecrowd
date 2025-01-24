# Entrada do caractere indicando a operacao
tipo_operacao = input().strip()

# Entrada da matriz 12x12
M = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input().strip()))
    M.append(linha)

# Elementos abaixo da diagonal principal
soma = 0
contador = 0
for i in range(12):
    for j in range(i):  # Somente elementos abaixo da diagonal principal
        soma += M[i][j]
        contador += 1

# Realizar a operacao solicitada
if tipo_operacao == 'S':
    resultado = soma
elif tipo_operacao == 'M':
    resultado = soma / contador

# Saida do resultado com 1 casa decimal
print(f"{resultado:.1f}")
