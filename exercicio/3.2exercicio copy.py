import os
os.system("cls || clear") 

QUANTIDADE_NOTA = 2 # constante
soma = 0

for i in range(QUANTIDADE_NOTA):
    while True:
        nota = float(input( f"digite {i+1}º nota: "))

        if nota >= 0 and nota <= 10:
            break # para o loco de repeticao.
    soma += nota

media = soma / QUANTIDADE_NOTA

print(f"media: {media}")
