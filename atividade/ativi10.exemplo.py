import os
os.system("cls || clear")

def entrega():
    quantidade_nota =3
    soma=0
    for i in range(quantidade_nota):
     while True:
        nota=float(input("digite a {i+1}º nota: "))
        if nota >=0 and nota <=10:
            print("")
            soma+=nota
            break
        else:
            print("tente novamente")
    media = soma/quantidade_nota
    return media

def verificacao():
    media = entrega()
    if media >=7:
        print("aprovador")
        print(f"media {media}")
    else:
        print("reprovador")
        print(f"media {media}")

verificacao()