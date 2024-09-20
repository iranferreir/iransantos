""""
Escreva um programa que solicite ao usuario o an de nascimento e, utilizando uma funcao, retorne com
a idade do ususario.
"""

import os
os.system("cls || clear")

data_nascimento= float(input("digite sua ano de nascimento: "))

def calcule(data):
    idade = 2024 - data
    return idade

resultado = calcule(data_nascimento)
print(resultado)