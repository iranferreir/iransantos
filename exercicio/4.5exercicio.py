import os
os.system("cls || clear") 

lista_numero = []
QUANTIDADE_NOTA =6
pares =0
impares =0

def verificar_pares_impares(numero):
    pares=0
    impares=0
    for numero in numero:
        if numero % 2 == 0:
            pares +=1
        else:
            impares +=1
    return pares, impares
print("\n=== Solicitando dades ===")             
for i in range(QUANTIDADE_NOTA):
    numero =float(input("digite o {i+1}º nnumero: "))
    lista_numero.append(numero)

#Processamento.
pares, importes = verificar_pares_impares(lista_numero)

#Saida.
print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_numero):
    print(f"{contador+1}º nota: {nota}")

print(f"\nQuantidade de pares: {pares}")
print(f"\nQuantidade de impares: {impares}")