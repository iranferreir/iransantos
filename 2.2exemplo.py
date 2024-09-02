import os
os.system("cls || clear")

while True:
    numero = int(input("digite um numero: "))
    if numero > 50 and numero % 7 == 0:
        print(numero)
        break
    