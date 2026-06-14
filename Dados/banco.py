import sys
import os

# Adiciona os caminhos necessários
sys.path.append(os.path.dirname(os.path.abspath(__file__)))         # .../PB-04/Dados/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # .../PB-04/

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import text

import pandas as pd
import produto_service

engine = create_engine("sqlite:///Dados/mercado.db", echo=True)

def criar_banco():
    class Base(DeclarativeBase):
        pass

    class Produto(Base):
        __tablename__ = "produtos"

        id = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=False)
        quantidade = Column(Integer, nullable=False)
        preco = Column(Float, nullable=False)

        def __repr__(self):
            return f"Produto(id={self.id}, nome={self.nome}, quantidade={self.quantidade}, preco={self.preco})"

    Base.metadata.create_all(engine)

def carregar_dados():
    df = pd.read_csv("Dados/produtos.csv")
    print(df)
    for _, row in df.iterrows():
        print(f"Inserindo produto: {row['nome']}, Quantidade: {row['quantidade']}, Preço: {row['preco']}")
        produto_service.incluir_produto(row['nome'], row['quantidade'], row['preco'])


def limpar_tabela_produtos():
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM produtos"))  # SQLite não suporta TRUNCATE
        connection.commit()

    

#criar_banco()
#carregar_dados()
#limpar_tabela_produtos()