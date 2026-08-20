"""Repositório de pessoas físicas usando SQLAlchemy ORM
para interagir com o banco de dados SQLite."""

from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.interfaces.pessoa_fisica_repository import (
    PessoaFisicaRepositoryInterface,
)


class PessoaFisicaRepository(PessoaFisicaRepositoryInterface):
    """Implementação do repositório de pessoas físicas usando SQLAlchemy ORM
    para interagir com o banco de dados SQLite."""

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert_person(  # pylint: disable=too-many-arguments
        self,
        *,
        renda_mensal: float,
        idade: int,
        nome_completo: str,
        celular: str,
        email: str,
        categoria: str,
        saldo: float
    ) -> None:
        with self.db_connection() as database:
            try:
                person = PessoaFisicaTable(
                    renda_mensal=renda_mensal,
                    idade=idade,
                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria_id=categoria,
                    saldo=saldo,
                )
                database.session.add(person)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_person_id(self, *, person_id: int) -> PessoaFisicaTable:
        with self.db_connection() as database:
            try:
                person = (
                    database.session.query(PessoaFisicaTable)
                    .filter(PessoaFisicaTable.id == person_id)
                    .one()
                )
                return person
            except NoResultFound:
                return None
