import os
os.system("cls || cleas") 

#Solicitando dades
float(input("digite o valor do produto"))

pagamento = input("""digite o numero correto de pagamento
1- pagamento a vista
2- pagamento a prazo
 """)

valor_final = 0
desconto = 0.10
             
#calculando
match(pagamento):
    case 1:
        print("valor do produto: {produto}")
        print("forma de pagamento: {a vista}")
        print("valor do desconto: {desconto}")
        print("total a pagar: {valor_final}")

    case 2:
        paceila = int(import("digite a quantidade de paceila que deseja parceilar(ate 6x):"))
        valor_paceira = produto / parceira
        print("valor do produto: {produto}")
        print("forma de pagamento: {a prazo}")
        print("quantidade de parceila: {parceila}")
        print("valor por parceila: {valor_parceila}")
        print("total a prazo: {produto}")
    case _:("opcao invalida! \n")