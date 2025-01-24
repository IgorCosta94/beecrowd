valor = float(input())
cem = cinquenta = vinte = dez = cinco = dois = 0
um = centavos_50 = centavos_25 = centavos_10 = centavos_5 = centavos_1 = 0

if 0 < valor < 1000000.00:
    # Converter para centavos para evitar problemas com ponto flutuante
    valor = round(valor * 100)
    
    # Notas
    cem = valor // 10000
    valor %= 10000

    cinquenta = valor // 5000
    valor %= 5000

    vinte = valor // 2000
    valor %= 2000

    dez = valor // 1000
    valor %= 1000

    cinco = valor // 500
    valor %= 500

    dois = valor // 200
    valor %= 200

    # Moedas
    um = valor // 100
    valor %= 100

    centavos_50 = valor // 50
    valor %= 50

    centavos_25 = valor // 25
    valor %= 25

    centavos_10 = valor // 10
    valor %= 10

    centavos_5 = valor // 5
    valor %= 5

    centavos_1 = valor // 1

    # Exibindo os resultados
    print("NOTAS:")
    print(f"{cem} nota(s) de R$ 100.00")
    print(f"{cinquenta} nota(s) de R$ 50.00")
    print(f"{vinte} nota(s) de R$ 20.00")
    print(f"{dez} nota(s) de R$ 10.00")
    print(f"{cinco} nota(s) de R$ 5.00")
    print(f"{dois} nota(s) de R$ 2.00")
    print("MOEDAS:")
    print(f"{um} moeda(s) de R$ 1.00")
    print(f"{centavos_50} moeda(s) de R$ 0.50")
    print(f"{centavos_25} moeda(s) de R$ 0.25")
    print(f"{centavos_10} moeda(s) de R$ 0.10")
    print(f"{centavos_5} moeda(s) de R$ 0.05")
    print(f"{centavos_1} moeda(s) de R$ 0.01")

