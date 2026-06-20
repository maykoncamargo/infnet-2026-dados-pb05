"""
O arquivo clientes_repository.py fará as funções de acesso ao banco de dados, 
ou seja, o CRUD completo propriamente dito. 
Os possíveis erros nessa camada devem ser repassados e tratadas pelas camadas superiores.

""" 
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import select
from Models.clientes import Cliente
from conectar_db import SessionLocal

def incluir_cliente(cliente):
    with SessionLocal() as session:
        session.add(cliente)
        session.commit()

def consultar_clientes():
    with SessionLocal() as session:
        return session.scalars(select(Cliente)).all()
    
def consultar_cliente(id):
    with SessionLocal() as session:
        return session.get(Cliente, id)

def alterar_cliente(id, cliente):
    with SessionLocal() as session:
        cliente_bd = session.get(Cliente, id)
        if cliente_bd:
            cliente_bd.nome = cliente.nome
            session.commit()

def excluir_cliente(id):
    with SessionLocal() as session:
        cliente = session.get(Cliente, id)
        if cliente:
            session.delete(cliente)
            session.commit()


#p = Cliente(id= None, nome="Cliente 199")
#incluir_cliente(p)
#print(consultar_clientes())
#print(consultar_cliente(1))
#alterar_cliente(4,p)
#excluir_cliente(1)
#print(consultar_clientes())