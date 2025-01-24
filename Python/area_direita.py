o=input()
m=[[0]*12]*12
total = 0
contador = 0
total2 = 0
contador2 = 0
for w in range(0,12,1):
    for x in range(0,12,1):
        #d=float(input())
        m[w][x]=10
        
for w in range(0,6):
    for x in range(12-w,12):
        total += m[w][x]
        contador +=1
        print("0",end=" ")
    print()
 
for w in range(6,11):
    for x in range(1+w,12):
        total2 += m[w][x]
        contador2 +=1
        print("0",end=" ")
    print()
    
if o == 'S':
    print(f"{total+total2:.1f}")
elif o == 'M':
    print(f"{(total+total2)/(contador+contador2):.1f}")
