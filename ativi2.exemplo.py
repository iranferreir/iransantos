import os
os.system("cls || clear")

#funcao com retorno.
def somar(n1, n2):
    soma = n1 +n2
    return soma

primeira_numero =int(input("digite um numero: "))
segundo_numero =int(input("digite um numero: "))

soma = somar(primeira_numero, segundo_numero)
print(f"soma: {soma}")