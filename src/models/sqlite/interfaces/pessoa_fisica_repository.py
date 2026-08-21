"""Módulo que define a interface do repositório de pessoas físicas no banco de dados SQLite."""

from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class PeopleRepository(ABC):
    """Interface para o repositório de pessoas físicas."""

    @abstractmethod
    def insert_person(  # pylint: disable=too-many-arguments
        self,
        *,
        renda_mensal: float,
        idade: int,
        nome_completo: str,
        celular: str,
        email: str,
        categoria: str,
        saldo: float,
    ) -> None:
        """Cria uma nova pessoa física no banco de dados."""

    @abstractmethod
    def get_person_id(self, *, person_id: int) -> PessoaFisicaTable:
        """Recupera uma pessoa física pelo ID."""
