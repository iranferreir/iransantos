import os
os.system("cls || clear")

senha=321
confirmacao_senha=123

while True:
    senha= input("digite sua senha:")
    confirmacao_senha= input("confimacao sua senha: ")
    if senha == confirmacao_senha:
        print(f"senha criada com suceco:")
        break            