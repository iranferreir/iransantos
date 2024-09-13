import os
os.system("cls || clear")

QUANTIDADE_NUMERO=3
lista_pares_positivo=0

# Entrada.
for i in range(QUANTIDADE_NUMERO):
    while True:
        numero = int(input(f"digite o {i+1}º numero: "))

        # verificando se o numero e par e positivo.
        if numero % 2==0 and numero > 0:
            lista_pares_positivo.append(numero)
            break
        else:
            print("Numero invalido. \mTente novamente.\n\n")

# Saida.
print("\n=== Exibimdo resultado ===")
for numero in reversed(lista_pares_positivo):
    print(numero)             