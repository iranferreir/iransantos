import os

os.system("cls || cleas")

#Solicitando dades
nome = input("digite seu nome:")
idade = int(input)("digite sua idade:")
peimeira_nota = float(input)("digite sua peimeira_nota:")
segunda_nota = float(input)("digite sua segunda_nota:")
terceira_nota = float(input)("digite sua terceira_nota:")
media = (peimeira_nota + segunda_nota + terceira_nota) / 3

if media <=7:
 print("o alumo sera reprovado")
else: 
 print("o aluno sera aprovado")

#verificando
print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"peimeira_nota: {peimeira_nota}")
print(f"segunda_nota: {segunda_nota}")
print(f"terceira_nota: {terceira_nota}")
print(f"media: {media}")