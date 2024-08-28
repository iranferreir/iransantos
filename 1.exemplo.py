import os
os.system("cls || clear") 

contador =0
continua ='s'

while continua =='s':
    #comandos a serem repetidos
    print("repentido....")

    contador +=1

    continua = input("tecle 's' se deseja continuar:").strip().lower()

if contador ==0:
    print("o bloco nao foi repetido")
else:
    print(f"o bloco foi repetido {contador}vezes")  