"""
Crie um programa qua solicite ao ususario seu login e uma senha
O programa deve continuar perdindo o login e a senha ate que ambos estejam corretos
O programa deve solicitar o login e senha apenas tres vexes. Caso ultrapasse o numero 
de tentativas, o programa deve ser finalizado.
    """

import os
os.system("cls || clesr")

login_salva = "ana"
senha_salva = "321"
contador = 0

while True:
    login = input("digite seu login: ")
    senha = input("digite sua senha: ")
    contador += 1

    if login_salva == login and senha_salva == senha:
       print("bem-vindo")
       break
    else:
       print("login ou senha invalidos.")     
       print(f"tentativa: {contador} \n")
       if contador == 3:
          break
print("=== FIM===")        