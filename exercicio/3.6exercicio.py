"""
Escreva um algoritmo que pergunte ao usuario se deseja inserir mais uma nota, se resposta
do usuario for "N", o programa fará a media aritmetica das notas informadas e mostrara a 
media aritmetica para o ususario.

Obs: Use um contador dentro do laco de repeticao para contar a quantidade de iteracoes(loops).
      """
import os
os.system("cls || clear")

soma =0
contador = 0

while True:
    nota = float(input("digite uma nota: "))
    contador += 1
    soma += nota
 
    resposta = input("digite inserir mais uma nota? ").upper()

    if resposta == "N":
        break

media =soma / contador
print(f"media: {media}")