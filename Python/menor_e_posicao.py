n=int(input())
x=list(map(int,input().split()))

menor=min(x)
posicao = x.index(menor)

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")
