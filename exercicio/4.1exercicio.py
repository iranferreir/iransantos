"""
Crie im programa que leia 3 notas, armazenando em um vetor e mostre as notas informadas.
"""
import os
os.system("cls || clear") 

lista_notas = []

for i in range(3):
    nota =float(input("digite uma nota: "))
    lista_notas.append(nota)

for nota in lista_notas:
    print(f"nota: {nota}")    
