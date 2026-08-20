"""Módulo de teste para o repositório PessoaFisicaRepository,
que lida com operações de banco de dados SQLite relacionadas a pessoas físicas."""

from src.models.sqlite.settings.connection import db_connection_handler
from .pessoa_fisica_repository import PessoaFisicaRepository

db_connection_handler.connect_to_db()


def test_insert_person():
    """Testa a inserção de uma pessoa física no banco de dados SQLite
    usando o repositório PessoaFisicaRepository."""

    renda_mensal = 5000.0
    idade = 31
    nome_completo = "test name"
    celular = "test phone"
    email = "test email"
    categoria = "test category"
    saldo = 1000.0

    repo = PessoaFisicaRepository(db_connection_handler)
    repo.insert_person(
        renda_mensal=renda_mensal,
        idade=idade,
        nome_completo=nome_completo,
        celular=celular,
        email=email,
        categoria=categoria,
        saldo=saldo,
    )
