import os
os.system("cls || clear")

soma =0

while True:
   primeira_nota = int(input("digite sua primeira_nota: "))
   segundo_nota = int(input("digite sua segunda_nota: "))
   terceira_nota = int(input("digite sua terceira_nota:"))
   soma = primeira_nota + segundo_nota + terceira_nota
   media = soma / 3

   if (primeira_nota < 0 or primeira_nota > 10) or (segundo_nota < 0 or segundo_nota > 10) or (terceira_nota < 0 or terceira_nota > 10):
      print("tente novamente")
   elif media >= 7:
      print("esta aprovado") 
      break
   elif media >= 5 or media <= 6.9:
      print("voce esta de recuperacao")
      break
   else:
      print("voce esta reprovado")
      break  
