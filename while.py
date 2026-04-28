contador = 0 

while True :
    numero = int(input("Digite um número: "))
    
    if numero >= 100 and numero <= 200:
        contador = contador + 1
    elif numero == 0:
        print(f"Você contou {contador}")
        break