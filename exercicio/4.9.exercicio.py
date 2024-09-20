import os
os.system("cls || clear")

QUANTIDADE_NUMERO=5
par_impar=[]
lista_numero=[]
lista_par=[]
lista_impar=[]
lista_positivo=[]
lista_negativo=[]

for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"digite o {i+1}º numero: "))
    par_impar.append(numero)

    if numero >=0:
        contador_par=+1
        par_impar.append(lista_positivo)
    else:
        contador_impar=+1
        par_impar.append(lista_negativo)

    if numero %2==0:
        contador_par =+1
        lista_par.append(contador_par)
    else:
        contador_impar =+1
        lista_impar.append(contador_impar)

print(f"Quantidade de numero pares: {lista_par}")
print(f"Quantidade de numero impares: {lista_impar}")
print(f"Quantidade de numero positivo: {lista_positivo}")
print(f"Quantidade de numero negativo: {lista_negativo}")