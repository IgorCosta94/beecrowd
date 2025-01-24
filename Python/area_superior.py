o=input()
m=[[0]*12]*12
total = 0
contador = 0
for w in range(0,12,1):
    for x in range(0,12,1):
        d=float(input())
        m[w][x]=d
        
for w in range(6,12):
    for x in range(12-i,i):
        total += m[w][x]
        contador +=1
    
if o == 'S':
    print(f"{total:.1f}")
elif o == 'M':
    print(f"{total/contador:.1f}")
