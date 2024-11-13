from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.database import db 

# Base para criar tabelas no branca dados.
Base = declarative_base()

class usuario(Base):
    __tablemame__ = "usuarios"

    id = Column(Integer, primary_key=True, autorincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    # Definindo caracteisticas da classe
    def__init__(self, nome: str, email: str, senha: str)
    self.nome =nome
    self.email = email
    self.senha = senha

# Criando tabela no branco dsdos
Base.metadata.create_all(bind=db)