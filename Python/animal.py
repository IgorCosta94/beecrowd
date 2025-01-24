classificação = input()
classe = input()
ordem = input()

if classificação == "vertebrado":
    if classe == "ave":
        if ordem == "carnivoro":
            print("aguia")
        elif ordem == "onivoro":
            print("pomba")
    elif classe == "mamifero":
        if ordem == "onivoro":
            print("homem")
        elif ordem == "herbivoro":
            print("vaca")
elif classificação == "invertebrado":
    if classe == "inseto":
        if ordem == "hematofago":
            print("pulga")
        elif ordem == "herbivoro":
            print("lagarta")
    elif classe == "anelideo":
        if ordem == "hematofago":
            print("sanguessuga")
        elif ordem == "onivoro":
            print("minhoca")    
    
