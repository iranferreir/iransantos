import os
os.system("cls || clear")

codigo_certo ="PROMO2024"
contador =0

while True:
    codigo = input("digite seu codigo de promacao: ")
    contador +=1
    if codigo == codigo_certo:
        print(f"codigo_certo: ")
        print(f"desconto recebido")
    elif codigo != codigo_certo:
        print("tente novamente") 

    elif contador == 3:    
        print("invalido")
        break    