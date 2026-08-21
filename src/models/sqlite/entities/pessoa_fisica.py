"""Módulo que define a tabela de pessoas físicas no banco de dados SQLite usando SQLAlchemy ORM."""

from sqlalchemy import Column, Integer, String, Float
from src.models.sqlite.settings.base import Base


class PessoaFisicaTable(Base):
    """Tabela para armazenar informações das pessoas físicas."""

    __tablename__ = "pessoa_fisica"

    id = Column(Integer, primary_key=True, autoincrement=True)
    renda_mensal = Column(Float, nullable=False)
    idade = Column(Integer, nullable=False)
    nome_completo = Column(String(100), nullable=False)
    celular = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    categoria = Column(String(20), nullable=False)
    saldo = Column(Float, nullable=False)

    def __repr__(self):
        return f"<PessoaFisica(id={self.id}, nome_completo='{self.nome_completo}', email='{self.email}')>"
