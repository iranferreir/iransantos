import os
os.system("cls || clear")

meta= int(input("digite uma meta de hora estudadas: "))
hora_estudadas=0

while True:
    hora_estudante= int(input("digite uma meta de hora estudadas:"))
    hora_estudante += hora_estudante
    if hora_estudante >= meta:
        print(f"hora estudadas: {meta}")
        print(f"total de hora estudadas: {hora_estudadas}")
        break