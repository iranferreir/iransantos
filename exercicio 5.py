import os
os.system("cls || cleas") 

print("""
# - codigo
      
1 - picanha R$ 25.00
2 - lasanha R$ 20.00
3 - stogonoff R$ 18.00
4 - bife acebolado R$ 15.00
5 - pao com ovo R$5.00
      """)

opcao = int(input("digite o valor do codigo: "))

match(opcao):
    case "1":
        print("picanha")
    case "2":
        print("lasanha")     
    case "3":
        print("stogonoff")
    case "4":
        print("bife acebolado")
    case "5":
        print("pao com ovo")
    case _:                                
        print("opcao invalido.")

        print("=== FIM ===") 
