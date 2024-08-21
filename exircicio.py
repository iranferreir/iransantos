import os
os.system("cls || cleas") 

#Solicitando dades

login = input("digite seu login: ")
senha = input("digite sua senha: ")

#verificando
login_correto = login == "Ana" # true
senha_correto = senha == "123" # false

if login_correto and senha_correto:
   print("bem-vindo")
else:
   print("login e senha invalita.")