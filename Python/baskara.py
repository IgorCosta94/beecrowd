import math

# Leia os três valores de ponto flutuante
A, B, C = map(float, input().split())

# Verifique se é possível calcular as raízes
if A == 0 or (B**2 - 4*A*C) < 0:
    print("Impossivel calcular")
else:
    # Calcule o discriminante
    delta = B**2 - 4*A*C

    # Calcule as raízes
    R1 = (-B + math.sqrt(delta)) / (2 * A)
    R2 = (-B - math.sqrt(delta)) / (2 * A)

    # Imprima as raízes com 5 casas decimais
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
