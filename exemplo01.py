import os
from dataclasses import dataclass
os.system("cls || clear") 

# Estrutura de dados.
@dataclass
class cliente:
    nome: str
    sobrinome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_CLIENTE =2

lista_cliente = []

print("\n=== Solicitando dados dos cliente ===")
for i in range(QUANTIDADE_CLIENTE): 
    cliente = cliente(
        nome = input("Digite seu nome: "),
        sobrinome = input("Digite seu sobrinome")
        idade = int(input("Digite sua idade: "))
        peso = float(input("digite seu peso: "))
        altura= float(input("digite sua altura: "))
    )                
    lista_cliente.append(cliente)
print("\n=== Exibindo dados dos cliente ===")

# Salva em um arquivo chamado: corteira_de_clintes.txt
nome_arquivo = "lista_de_cliente.txt"
    
# Fazer leitura de dados do arquivo carteira_de clientes.txt e mostre no terminal. 
with open(nome_arquivo, "a") as arquivo_cliente:
    for cliente in arquivo_cliente:
        arquivo_cliente.write(f"{cliente.nome}, {cliente.sobrinome}, {cliente.idade}, {cliente.peso}, {cliente.altura}\n")
        
arquivo_cliente.close()        



