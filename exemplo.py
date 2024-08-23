import os
os.system("cls || cleas") 

#solicitando dades.
numero = int(input("digite um numero para tabuada:"))

print(f"\ntaduada de multiplicacao do numero: {numero}")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
