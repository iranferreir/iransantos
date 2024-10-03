import os

os.system("cls || cleas")

#Solicitando dades
primeiro_numero = float(input("digite seu primeiro_numero: "))
segundo_numero = float(input("digite seu segundo_numero: "))

#calculando
soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
media = (primeiro_numero + segundo_numero) /2

if (primeiro_numero > segundo_numero):
   nemor_numero = segundo_numero
else:
   nemor_numero = primeiro_numero

if (segundo_numero > primeiro_numero):
   maior_numero = segundo_numero
else:
   maior_numero = segundo_numero

#exibindo dades
print(f"primeiro_numero: {primeiro_numero}")
print(f"segundo_numero: {segundo_numero}")  
