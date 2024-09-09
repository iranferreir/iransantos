import os
os.system("cls || clear")

def calcula_peso():
    peso=float(input("peso: ")) 
    return peso
def calcula_altura(): 
    altura=float(input("altura: "))
    return altura
def IMC ():
    while True:
        peso= calcula_peso
        altura= calcula_altura
        IMC=peso/(altura*altura)
        if IMC<18.5:
            print("abaixo do peso: conslte um nutricionista para orientacao.")
        elif IMC<=24.9:
            print("peso nomal: mantenha habitos saudaveis.")
        elif IMC<=29.9: 
            print("sobrepeso: considere umadieta balanceada e atividade fisica.")
        elif IMC<=34.9:
            print("obesidade grau 1: procure orientacao de um profissional de saude.")
        elif IMC<=39.9:
            print("obesidade grau 2: consulte um medico para avaliacao e orientacao.")
        elif IMC<=40.0:
            print("obesidade grau 3: busque assistencia medica imediatamente. ")

IMC()
                    