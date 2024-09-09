import os
os.system("cls || clear")

numero = int(input("digite um numero: "))

def pares_impares(n1:int):
    # pares =0
    # impares =0
    if n1 % 2== 0:
       # pares += 1
        print("par")
    else:
        # impares += 1
        print("impares")
    # return pares, impares

resutado = pares_impares(numero) 
        