# Leia o tipo de chá verdadeiro
T = int(input("Digite o tipo de chá (1 a 4): "))

# Leia as respostas dos competidores
respostas = list(map(int, input("Digite as respostas dos 5 competidores (1 a 4) separadas por espaço: ").split()))

# Verifique o número de respostas corretas
corretas = respostas.count(T)

# Exiba o número de respostas corretas
print(corretas)

