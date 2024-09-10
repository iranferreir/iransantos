"""
Crie um programa qua solicite ao usuario seu login e uma senha
O programa deve continuar pedindo o login e a senha ate que ambos estejam corretos.
"""

import os
os.system("cls || clear") 

logi_salve = "ana"
senha_salve = "321"

while True:
    login = input("digite seu login: ")
    senha = input("digite sua senha: ")

    if input("login_salve == login and senha_salve == senha"):
       print("bem,-vindo")
       break
    else:
       print("tente novamente")

    