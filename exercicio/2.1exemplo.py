import os
os.system("cls || clear")

numero=0

while True:
    numero = int(input("digite seu numero: "))
    if numero < 0:
        contador =+1       
    elif numero >=0:
        break
    
print(f"quantidade do numero negativo: { contador}")