from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

class Produto(Base):
    __tablename__ = "clientes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f"{self.id},{self.nome}"
    
    #permite imprimir o valor do objeto instanciado em listas
    def __repr__(self):
        return self.__str__()
