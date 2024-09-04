import os
os.system("cls || clear")

contador=0
soma = 0
VALOR_MAXIMO=200

while True:
    numero =int(input("digite um numero: "))
    if numero % 2==0:
        soma += numero
        contador+=1

    elif soma > VALOR_MAXIMO:
        break

print(f"total de numero impares: {contador}")
print(f"soma: {soma}")
