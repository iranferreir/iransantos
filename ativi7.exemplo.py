import os
os.system("cls || clear")


preco = float(input("digite o preco do produto: "))

def produto(num1):
    if num1 < 100:
        num1 * 0.10
    
    if num1 >= 100:
        num1 * 0.20
        return num1
    
resultado = produto(preco) 
print("{resultado} reais")         