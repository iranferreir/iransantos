import os
os.system("cls || clear")

contador_par =0
contador_impar =0

for i in range(6):
    numero = int(input("digite o {1 + 1}º numero: "))

def par(numero):
    total = numero %2 == 0 
    contador_pares +=1
    return total 

def impar(numero):
    total = numero %2 == 0
    contador_impares +=1
    return total

total = par(numero)
print(f"par")

        