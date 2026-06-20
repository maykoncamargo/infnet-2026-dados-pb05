from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

class Produto(Base):
    __tablename__ = "produtos"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    quantidade: Mapped[int]
    preco: Mapped[float]

    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.id},{self.nome},{self.quantidade},{self.preco}"
    
    #permite imprimir o valor do objeto instanciado em listas
    def __repr__(self):
        return self.__str__()
