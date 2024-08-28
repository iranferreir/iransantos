import os
os.system("cls || clear") 

nota1= 0

nota2 = 0

while True:
    nota1 = float(input("digite sua nota1: "))
    nota2 = float(input("digite sua nota2: "))

    if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
        print("\nA nota deve ser maior ou iqual a 0 e menor e iqual a 10 ")
    else:
        break

nota_final = nota1 + nota2
media = nota_final / 2

print(f"media_final do aluno {media} ")        

