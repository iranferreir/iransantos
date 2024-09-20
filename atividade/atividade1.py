import os
os.system("cls || clear")

#funcao
def calcular_media(primeiro_numero, segundo_numero):
    soma= primeiro_numero + segundo_numero
    resultado = soma / 2
    return resultado

primeiro_numero= int(input("digite um numero: "))
segundo_numero= int(input("digite um numero: "))

media= calcular_media(primeiro_numero, segundo_numero)

print(f"media: {media}")