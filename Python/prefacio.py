def calcular_quo_resto(a, b):
    if b == 0:
        return "Erro: divisor 0"  # Evitar divisão por zero
    
    q, r, result = 0, 0, 0

    if a < 0 and b > 0 and a != b:
        result = b
        for q in range(1, abs(a) + 1):  # Ajuste para evitar loop infinito
            if -b * q <= a:
                result = -b * q
                break
        r = a - result
        q = 1 - q
    elif a < 0 and b < 0 and a != b:
        result = b
        for q in range(1, abs(a) + 1):
            if b * q <= a:
                result = b * q
                break
        r = a - result
        q = q - 1
        if a > b and q == 0:
            q += 1
    elif a > 0 or a == b:
        q = a // b
        r = a % b
    if r < 0:
        r = -r

    return q, r





        

