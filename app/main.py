from services.usuario_service import usuarioservice
from repositories.usuario_repositories import usuarioRepository
from config.database import session
import os

session = session()
repository = usuarioRepository(session)
service = usuarioservice(repository)

# Limpa o ternimal.
os.system("cls || clear")

# Solicitando daods para o usuario.
print("\mCadastrado usuario: ")
nome = input("digite seu nome: ")
email = input("digite seu email: ")
senha = input("digite sau senha: ")

service.criar_usuario(nome, email, senha)

# Exibindo todos os registros na tabela "usuario" do branco de dados.
print("\n=== Listando usuario cadastrados ===")
lista_usuario = service.lista_todos_usuario()
for usuario in lista_usuario:
    print(f"Nome: {usuario.nome} \nE-mail: {usuario.email}")