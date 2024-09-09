"""
Escreva um programa que permita ler 2 notas de um aluno e:

-Informe por meio de uma funcao a media;

-Informe por meio de uma funcao se a media for maior ou igual a 7, o aluno estara aprovado, caso contrario, estara
reprovado.
"""
import os
os.system("cls || clear")

pimeira_nota= int(input("digite o  pimeira nota: "))
segunda_nota= int(input("digite o segundo nota: "))

QUANTIDADE_NOTAS = 2

def media (num1, num2):
    media = (num1 + num2) / QUANTIDADE_NOTAS
    if media >= 7:
       print("aprovado")

def media (num1, num2):
    media = (num1 + num2) / QUANTIDADE_NOTAS
    if media < 7:
        print("reprovado")

media(pimeira_nota, segunda_nota)
media(pimeira_nota, segunda_nota)