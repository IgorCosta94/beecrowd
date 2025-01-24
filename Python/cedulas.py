valor = float(input())
cem = cinquenta = vinte = dez = cinco = dois = 0
um = centavos_50 = centavos_25 = centavos_10 = centavos_5 = centavos_1 = acumulador =0

if valor > 0 and valor < 1000000.00:
    while acumulador < valor:
        if acumulador + 100 <= valor:
            acumulador += 100
            cem += 1
        elif acumulador + 50 <= valor:
            acumulador += 50
            cinquenta += 1
        elif acumulador + 20 <= valor:
            acumulador += 20
            vinte += 1
        elif acumulador + 10 <= valor:
            acumulador += 10
            dez += 1
        elif acumulador + 5 <= valor:
            acumulador += 5
            cinco += 1
        elif acumulador + 2 <= valor:
            acumulador += 2
            dois += 1
        elif acumulador + 1 <= valor:
            acumulador += 1
            um += 1
        elif acumulador + 0.50 <= valor:
            acumulador += 0.50
            centavos_50 += 1
        elif acumulador + 0.25 <= valor:
            acumulador += 0.25
            centavos_25 += 1
        elif acumulador + 0.10 <= valor:
            acumulador += 0.10
            centavos_10 += 1
        elif acumulador + 0.05 <= valor:
            acumulador += 0.05
            centavos_5 += 1
        elif acumulador + 0.01 <= valor:
            acumulador += 0.01
            centavos_1 += 1       
print("NOTAS:")
print(f"{cem} nota(s) de R$ 100.00")
print(f"{cinquenta} nota(s) de R$ 50.00")
print(f"{vinte} nota(s) de R$ 20.00")
print(f"{dez} nota(s) de R$ 10.00")
print(f"{cinco} nota(s) de R$ 5.00")
print(f"{dois} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"calculo simples.exe00")
print(f"{centavos_50} moeda(s) de R$ 0.50")
print(f"{centavos_25} moeda(s) de R$ 0.25")
print(f"{centavos_10} moeda(s) de R$ 0.10")
print(f"{centavos_5} moeda(s) de R$ 0.05")
print(f"{centavos_1} moeda(s) de R$ 0.01")

