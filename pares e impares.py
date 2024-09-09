import os
os.system("cls || clear") 

pares = 0
impares = 0

for i in range(6):
    numero = int (input("digite um numero: "))

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print(f"quantidade de pares: {pares}")
print(f"quantidade de impares: {impares}")
