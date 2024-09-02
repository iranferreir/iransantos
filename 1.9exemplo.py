import os
os.system("cls || clear")

num_linhas= 4
num_colunas= 6

#laco para cada linha
for i in range(num_linhas):
    #laco para cada coluna dentro da linha
    for j in range(num_colunas):
        #inprine um asterisco sem pular linha
        print('*', end='')
    print()    