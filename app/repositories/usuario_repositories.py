from models.usuario_models import usuario
from sqlalchemy.orm import session

class usuarioRepository:
    def __init__(self, session: session):
        self.session = session

    def salva_usuario(self, usuario: usuario):
        self.session.add(usuario)
        self.session.comit()

    def pesquisar_usuario_por_email(self, email: str):
        return self.session.query(usuario).filter_by(email = email).first()

    def excluir_usuario(self, usuario: usuario):
        self.session.delete(usuario)
        self.session.commit()

    def atualizar_usuario(self, usuario: usuario)            
        self.session.commit()
        self.session.refresh(usuario)

    def lista_usuario(self):
        return self.session.query(usuario).all()    