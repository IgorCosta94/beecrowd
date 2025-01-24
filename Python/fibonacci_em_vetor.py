t=int(input())

for a in range(0,t,1):
    x=int(input())
    x = abs(x)
    n1 = 0
    n2 = 1
    soma= 0
    if x == 0:
        print("Fib(0) = 0")
    elif x == 1:
        print("Fib(1) = 1")
    elif x > 1:
        for b in range(2,x+1,1):
            soma = n1 + n2
            n1 = n2
            n2 = soma
        print(f"Fib({x}) = {soma}")
