import os
os.system("cls || clear")

QUANTIDADE_NUMERO=5
lista_numero=[]

def verificando_numero(lista_numero):
    lista_numero =[]

    for numero in lista_numero:
        #verificando se o numero informado e negativo.
        if numero <0:
            # Caso o numero seja negativo,
            # Sera substituido por zero.
            numero =0
        lista_numero.append(numero)
    
    return lista_numero

print("=== Solicitando dades ===")
for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"digite o seu {i+1}º numero: "))
    
    # Inserindo numero no vetor
    lista_numero.append(numero)

lista_numero = verificando_numero(lista_numero)

print("\n=== Exibindo dades ===")
for cada_numero in lista_numero:
    print(cada_numero)      
