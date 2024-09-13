import os
os.system("cls || clear")

QUANTIDADE_NUMERO=4
lista_numero=0

for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"digite o {i+1}º numero: "))
    lista_numero.append(numero)

def calcula(a):
    positivos= a >=0
    par = a % 2==0
    return par, positivos

lista = calcula(lista_numero)
for numero in lista_numero
    print(lista_numero)