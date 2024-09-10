"""
Escreva um algoritmo que pergunte ao ususario se deseja inserir mais uma nota. Mostre um menu 
conforme o descrito abaixo:

S - Inserir mais uma nota:
P - Ver quantas notas foram inseridas:
N - Calcular a media aritmetica das notas informadas.

O programa deve mostrar a media aritmetica parao ususario.
"""

import os
os.system("cls || clear")

soma: float =0
quantidade_nota =0

while True:
    print("=== NENU ===")
    print("S - Inserir mais uma nota")
    print("P - Ver quantas notas foram inseridas")
    print("N - Calcular a media aritmetica das notas informadas")

    resposta = input("digite inserir uma nota: ").upper()

    match resposta:
        case "S":
            nota = float(input("\nDigite uma nota: "))
            soma += nota
            quantidade_nota +=1
        case "P":
            if quantidade_nota == 0:
                print("noa foram inseridos a notas. \n")
                input("prossione uma tecla para continuar...")
                timo.sleep(3)
            else:
                print(f"quantidade de notas inseridas: {quantidade_nota} \n")
                    

