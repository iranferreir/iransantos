import os
os.system("cls || clear") 

nota = float(input("digite sua nota:"))

while nota < 0 and nota > 10:
    print("\nA nota deve ser maior ou iqual a 0 e menor e iqual a 10")
    nota - float(input("digite uma nota: "))

print(f"nota: {nota}")    