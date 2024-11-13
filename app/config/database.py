from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextlib

# Definindo parametros para acesso ao branco de dados.
db_user = "aluno"
db_pasword = "aluno_senha"
db_name = "meu_branco_senai"
db_host = "localhost"
db_port = "3306"

# Endereco (URL) para conexao com branco de dados.
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_pasword}@{db_name}:{db_host}:{db_port}/"

# Criando branco de dados.
db = create_engine(DATABASE_URL)

# Criando conexao com branco de dados.
session = sessionmaker(bind=db)
session = session()

# Gerenciando conexao com branco dados.
@contextmanager
def get_db():
    db = session()
    try:
        yield db
        db.commit() #Salvador
    except Exception as erro:
        db.rollback() # Caso ocorra algum erro, desfaz alterações no BD.
        raise erro # Caso ocorra algum erro, mostra mensagem de erro no terminal
    finally:
        db.close() # Fecha conexao com BD.
