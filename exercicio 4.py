import os
os.system("cls || cleas") 

primeira_numero = int(input("digite o primeiro_numero:"))
segundo_numero = int(input("digite o segundo_numero:"))
opcao = input("digite uma opcao( + - * /): ")

match(opcao):

    case "+": 
        resultado = primeira_numero + segundo_numero
    case "-":    
        resultado = primeira_numero - segundo_numero  
    case "/":
        resultado = primeira_numero / segundo_numero
    case "*":
        resultado = primeira_numero * segundo_numero
    case _:
        print("opcao invalida.")

print(f"resultado: {resultado}")
print("=== FIM ===")                        