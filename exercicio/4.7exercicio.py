import os
os.system("cls || clear")

QUANTIDADE_NUMERO=4
lista_numero=[]

print("=== Solicitando dades ===")
for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"digite o seu {i+1}º numero: "))
    lista_numero.append(numero)

def calcule(lista_numero):
    lista_numero()
    for negativa in lista_numero:
        if numero < 0:
            numero =0

        lista_numero.append(numero)
        return lista_numero        
lista_numero = calcule(lista_numero)
for numero in lista_numero:
    print(numero)