import os
os.system("cls || clear")

#Entrada.
lista_numero = []
QUANTIDADE_NOTA =4
negativos =0
positivos =0

print("\n=== Solicitando dades ===") 
for i in range(QUANTIDADE_NOTA):
    numero =float(input("digite o {i+1}º nnumero: "))
    lista_numero.append(numero)

#Processamento.
if numero <10:
    negativos.append(numero)
else:
    positivos.append(numero)

#comando len() - retorna a quantidade de elementos no vetor/lista.
QUANTIDADE_NEGATIVOS =len(negativos)

#comando sum() - retorna a soma dos elementos no vetor/lista.
soma_positivos = sum(positivos)

#Saida.
print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_numero):
    print(f"{contador+1}º nota: {nota}")

print(f"\nQuantidade de negativos: {QUANTIDADE_NEGATIVOS}")
print(f"\nSoma de positivos: {soma_positivos}")