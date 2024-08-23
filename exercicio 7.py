import os
os.system("cls || cleas") 

print("""
1- janeiro
2- fevereiro
3- março
4- abril
5- maio
6- junho
7- julho
8- agosto
9- setembro
10- oitubro
11- novenbro
12- dezembro
     """)

mes = int(input("digite o numero do mes correspondeto ao mes"))

match(mes):
    case 1:
        print("janeiro")
    case 2:
        print("fevereiro")
    case 3:
        print("março")
    case 4:
        print("abril")
    case 5:
        print("maio")
    case 6:
        print("junho")
    case 7:
        print("julho")
    case 8:
        print("agosto")
    case 9:
        print("setembro")
    case 10:
        print("oitubro")
    case 11:
        print("novembro")
    case 12:
        print("dezembro")        
