import os
os.system("cls || clear") 

#Entrada.
lista_numero = []
QUANTIDADE_NOTA =5

for i in range(QUANTIDADE_NOTA):
    numero =float(input("digite o {i+1}º nnumero: "))
    lista_numero.append(numero)

#Processamento.
maior_numero = max(lista_numero)
menor_numero = min(lista_numero)

#Saida.
print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_numero):
    print(f"{contador+1}º nota: {nota}")

print(f"\nMenor numero: {menor_numero}")
print(f"\nmaioe numero: {maior_numero}")