import os
os.system("cls || cleas") 

peso_ideal = 0
altura = float(input("digite sau altura:"))
sexo = input("digite o caractere correspondente ao seu sexo:"). upper()

match(sexo):
    case "M":
        peso_masculino = (72.7 * altura) - 58
        print(f"peso ideal: (peso_masculino: 2f) Kg")
    case "F":
        pseo_feminino = (62.1 * altura) - 44.7
        print(f"peso ideal: (peso_feminino: 2f)  Kg")   
    
        print("opcao invalido")    
