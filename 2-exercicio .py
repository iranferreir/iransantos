import os
import time

os.system("cls || cleas") 

media =0 

for i in range(3):
    nota = float(input("digite a {i+0}º nota: "))
    media= nota + media

media = media/3

if media >=7:
    print(f"sua media e {media}")
if media>= 4 and media<7:
    print(f"voce esta reprovado, sua media e {media} ")
else:
    print("voce foi aprovado")                        