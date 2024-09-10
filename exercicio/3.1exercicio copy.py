import os
os.system("cls || clear") 

while True:
    nota = float(input("digite sua nota:"))

    if nota < 0 and nota > 10:
        print("\nA nota deve ser maior ou iqual a 0 e menor e iqual a 10")
    else:
        break # para o laco de repeticao.
    
print(f"nota: {nota}")    