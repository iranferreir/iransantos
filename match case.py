import os
os.system("cls || cleas") 

print("""
1 - cadastrar usuário
2 - excluir usuário
3 - saior do sistema
      """)

opcao = int(input("digite uma opcao: "))

match(opcao):
    case 1:
        print("opcao de cadestrar usuario.")
    case 2:
        print("opcao de excluir usuario.")
    case 3:
        print("opcao de sair do sistema.") 
    case _: 
        print("opcao invalido.")

        print("===FIM===")         