from sqlalchemy import select
from sqlalchemy.orm import Session

from typing import Generic, Type, TypeVar

from unittest.mock import Base


T = TypeVar("T", bound=Base)

class RepositorioBase(Generic[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

#CRUD
def adicionar(self, objeto: T) -> T:
    """Adicionar à sessão e faz flush para o dados gerar o id (sem fazer commit)"""
    self.db.add(objeto)
    self.db.flush()
    self.db.refresh(objeto)
    return objeto

def obter_por_id(self, id: int) -> T | None:
    return self.db.get(self.model, id)

def remover(self, objeto: T) -> None:
    self.db.delete(objeto)
    self.db.flush() 

def listar_todos(self) -> list[T]:
    return self.db.query(self.model).all()