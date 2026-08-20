"""Configuração da conexão com o banco de dados SQLite."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Classe responsável por gerenciar a conexão com o banco de dados SQLite."""

    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    def connect_to_db(self):
        """Estabelece a conexão com o banco de dados SQLite."""
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        """Retorna o objeto engine do SQLAlchemy."""
        return self.__engine

    def __enter__(self):
        """Método chamado ao entrar no contexto do gerenciador de contexto."""
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Método chamado ao sair do contexto do gerenciador de contexto."""
        self.session.close()


db_connection_handler = DBConnectionHandler()
