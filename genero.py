contadorM = 0
contadorF = 0

while True:
    genero = input("Qual é seu gênero? ").upper()
    if genero == "M":
        contadorM +=1
    elif genero == "F":
        contadorF +=1
    elif genero == "NENHUM":
        break
print(f"Tem {contadorM} homens e {contadorF} mulheres")