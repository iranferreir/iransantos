import os
os.system("cls || clear")

soma_calorias =0
limite_calorias=2000
print(f"limite de calorias para consumir: ")

while True:
    calcula=int(input("digite a quantidade de calcula cinsumidas: "))
    soma_calorias += calcula
    execesso_calculas = soma_calorias - limite_calorias
    if soma_calorias > limite_calorias:
        print(f"total de calorias: {soma_calorias}")
        print(f"excesso de calorias: {execesso_calculas}")
        break
