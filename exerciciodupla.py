"""
ALUNO - Iran ferreira dos santos
"""

import os
from dataclasses import dataclass
os.system("cls || clear") 

@dataclass
class dados:
    idade:set
    sexo:int
    salario:float

@dataclass
class final:
    lista_final:list 

def menu():       
    print("""
Codigo | Descricão
   1   | Adicionar pessoa   
   2   | Exibir resultados
   3   | Sair
""")   

def limpar_tela():
    os.system("Cls || Clear")

def criando_arquivo(a, b):
    with open(a,"a") as arquivo_habitantes:
        for habitantes in b:
            arquivo_habitantes.write(f"{habitantes.idade},{habitantes.sexo},{habitantes.salario}\n")
            arquivo_habitantes.close()   

def criando_arquivo_final(a, b):
    with open(a,"a") as arquivo_habitantes:
        for habitante in b:
            arquivo_habitantes.write(f"{habitante}, \n")
            arquivo_habitantes.close()

def lendo_arquivos(a):
    with open(a,"r") as lendo_habitantes:
        for linha in lendo_habitantes:
            idade, sexo, salario = linha.strip().split(",")
            lista_final.append(habitantes(idade = int(idade),sexo = sexo, salario = float(salario)))
        lendo_habitantes.close()
    return lista_final    
             
def media(a):
    QUANTIDADE= len(a)
    soma = sum(a)
    if QUANTIDADE == 0:
        return 0
    else:
        media = soma / QUANTIDADE
        return media
    
while True:
    lista_final = []    