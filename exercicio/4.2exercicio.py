"""
Crie um programa que leia 3 notas, armazanando em um vetir e calcule a media aritmetica.
Monter as 3 notas informadas pelo ususario e informe a media.
"""

import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 3
lista_notas = []

for i in range(3):
    nota = float(input("digite uma nota: "))
    lista_notas.append(nota)

soma = nota
media = soma / QUANTIDADE_NOTAS

print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_notas):
    print(f"{contador+1}º nota: {nota}")

print(f"media: {media}")