import sys
import os

# Adiciona os caminhos necessários
sys.path.append(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy import text

import pandas as pd
import Service.produto_service as produto_service
import Service.cliente_service as cliente_service

from Models.produto import Base as Base_produto
from Models.clientes import Base as Base_cliente

engine = create_engine("sqlite:///Dados/mercado.db", echo=True)


def criar_banco():
    Base_produto.metadata.create_all(engine)
    Base_cliente.metadata.create_all(engine)
    print("Banco Criado com Sucesso")


def carregar_dados_produtos():
    df = pd.read_csv("Dados/produtos.csv")
    for _, row in df.iterrows():
        print(f"Inserindo produto: {row['nome']}, Quantidade: {row['quantidade']}, Preço: {row['preco']}")
        produto_service.incluir_produto(row['nome'], row['quantidade'], row['preco'])


def carregar_dados_clientes():
    df = pd.read_json("Dados/clientes.json")
    for _, row in df.iterrows():
        print(f"Inserindo cliente: {row['nome']}")
        cliente_service.incluir_cliente(row['nome'])


def limpar_tabela_produtos():
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM produtos"))
        connection.commit()


def limpar_tabela_clientes():
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM clientes"))
        connection.commit()


def limpar_tabelas():
    limpar_tabela_produtos()
    limpar_tabela_clientes()


def carregar_dados():
    carregar_dados_produtos()
    carregar_dados_clientes()


#criar_banco()
#carregar_dados_produtos()
#carregar_dados_clientes()
#limpar_tabela_produtos()
#limpar_tabela_clientes()


#criar_banco()
#carregar_dados()
#limpar_tabelas()
