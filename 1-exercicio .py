import os
import time

os.system("cls || cleas") 

soma =0
media =0

for i in range(4):
    nota = int(input(f"informe a {i+1}º: "))
    soma = nota + soma
    time.sleep(1)

media = soma/4
print(f"sua media e {media}")         