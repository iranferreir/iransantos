import os
os.system("cls || clear") 

#Entrada.
lista_notas = []

for i in range(2):
    nota = float(input("digite uma nota: "))
    lista_notas.append(nota)

#Saida.
for nota in lista_notas:
    print(f"nota: {nota}")     