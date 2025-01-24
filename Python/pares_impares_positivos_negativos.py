cont_par = 0
cont_impar = 0
cont_positivos = 0
cont_negativos = 0
for w in range(1,6,1):
    x = int(input())
    if x % 2 == 0:
        cont_par += 1
    if x % 2 == 1:
        cont_impar += 1
    if x > 0:
        cont_positivos += 1
    if x < 0:
        cont_negativos += 1
print(f"{cont_par} valor(es) par(es)")
print(f"{cont_impar} valor(es) impar(es)")
print(f"{cont_positivos} valor(es) positivo(s)")
print(f"{cont_negativos} valor(es) negativo(s)")        
