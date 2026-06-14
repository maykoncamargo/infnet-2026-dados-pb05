"""
O arquivo produto_repository.py fará as funções de acesso ao banco de dados, 
ou seja, o CRUD completo propriamente dito. 
Os possíveis erros nessa camada devem ser repassados e tratadas pelas camadas superiores.

""" 
from sqlalchemy import select
from models import Produto
from conectar_db import SessionLocal

def incluir_produto(produto):
    with SessionLocal() as session:
        session.add(produto)
        session.commit()

def consultar_produtos():
    with SessionLocal() as session:
        return session.scalars(select(Produto)).all()
    
def consultar_produto(id):
    with SessionLocal() as session:
        return session.get(Produto, id)

def alterar_produto(id, produto):
    with SessionLocal() as session:
        produto_bd = session.get(Produto, id)
        if produto_bd:
            produto_bd.nome = produto.nome
            produto_bd.preco = produto.preco
            produto_bd.quantidade = produto.quantidade
            session.commit()

def excluir_produto(id):
    with SessionLocal() as session:
        produto = session.get(Produto, id)
        if produto:
            session.delete(produto)
            session.commit()




#p = Produto(id= None, nome="Coca-cola", preco=10.0, quantidade=100)
#incluir_produto(p)
#print(consultar_produtos())
#print(consultar_produto(1))
#alterar_produto(2,p)
#excluir_produto(1)
#print(consultar_produtos())