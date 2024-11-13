from models.usuario_models import usuario
from repositories.usuario_repositories import usuarioRepository

class usuarioService:
    def __init__(self, respository: usuarioRepository)
        self.repository = respository

    def criar_usuario(self, nome: str, email: str, senha: str)
        try:
            usuario = usuario(nome=nome, email=email, senha=senha)

            usuario_cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if usuario_cadastrado:
                print("usuario ja cadastrado!")
                return
            
            self.repository.salva_usuario(usuario)
            print("usuario cadastrado com sucesso!")
        except TypeError as erro:
            print(f"erro ao salva usuario: {erro}")
        except Exception as erro:
            print(f"ocorreu um erro inesperado: {erro}")

    def lista_todos_usuario(self):
        return self.repository.lista_usuario()                