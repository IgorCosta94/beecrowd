teste=int(input())

for w in range(0,teste,1):
    nome,forca=input().split()
    forca=int(forca)
    if nome == 'Thor':
        print("Y")
    else:
        print("N")
