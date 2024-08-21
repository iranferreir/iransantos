import os
os.system("cls || cleas") 

print("""
1 - domingo           
2 - segunda-feira 
3 - terca-feira
4 - quarta-feira
5 - quinta-feira
6 - sexta-feira
7 - sabado
      """)

dia = int(input("digite o dia util: "))

match(dia):
    case 1:
        print("final de semana")
    case 2:
        print("dia util")
    case 3:
        print("dia util")
    case 4:
        print("dia util")
    case 5:
        print("dia util")
    case 6:
        print("dia util")
    case 7:
        print("comeco da semama") 
    case _:
        print("opcao invalido")    

