import os
os.system("cls || clear") 

QUANTIDADE_NOTA = 4
lista_nota=[]

for i in range(QUANTIDADE_NOTA):
    nota =float(input("digite a soma {i+1}º nota: "))
    lista_nota.append(nota)

soma = sum(lista_nota)
media = soma / QUANTIDADE_NOTA

if media >=7:
    situado = "aprovado"
elif media >=5 and media < 7:
    situado = "recuperacao"
else:
    situado = "reprovado"

print(f"resultado: {situado}")
