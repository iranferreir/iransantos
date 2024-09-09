import os
os.system("cls || clear")

peimeiro_numero = int(input("digite um numero: "))
segundo_numero = int(input("digite um numero: "))
opcao = int(input("digite uma opcao "))

def operacao(n1: int, n2: int, opcao: int):
    match(opcao):
        case"1":
            resutador= n1 + n2
        case "2":
            resutador = n1 - n2
        case"3":
            resutador = n1 / n2 
        case"4":
            resutador = n1 * n2
        case _:
            print("opcao invalida")    
    return resutador

resutado = operacao(peimeiro_numero, segundo_numero,opcao)
print(resutado)