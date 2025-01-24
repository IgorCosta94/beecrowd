total = 0
contador = 0
total2 = 0
contador2 = 0
o = input().strip()

# Entrada da matriz 12x12
m = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input().strip()))
    m.append(linha)
        
for w in range(1,6):
    for x in range(0,w):
        total += m[w][x]
        contador +=1
 
for w in range(6,11):
    for x in range(0,11-w):
        total2 += m[w][x]
        contador2 +=1
    
if o == 'S':
    print(f"{total+total2:.1f}")
elif o == 'M':
    print(f"{(total+total2)/(contador+contador2):.1f}")
