import os
os.system("cls || clear")

num_inicial = 2
contador =0

while True:
    numero = int(input("digite um numero: "))
    produto = numero + num_inicial
    contador +=1
    if produto > 100:
        print(f"produto: {produto} ")
        print(f"multiplicacao realizado: {contador} ")
        break