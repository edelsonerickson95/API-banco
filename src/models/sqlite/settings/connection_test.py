"""Testes para a conexão com o banco de dados SQLite."""

import pytest
from sqlalchemy.engine import Engine
from .connection import db_connection_handler

@pytest.mark.skip(reason="interacao com banco")
def test_connection_to_db():
    """Testa a conexão com o banco de dados SQLite."""
    assert db_connection_handler.get_engine() is not None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
