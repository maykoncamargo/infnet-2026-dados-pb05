"""
O arquivo produto_crud.py é um arquivo que permitirá às operações de CRUD na tabela de produtos do banco de dados. 
A ideia é permitir que o administrador do sistema faça alguma correção necessária na tabela de produtos. 
O seu programa não é obrigado a utilizar esse arquivo como a camada de interface com o usuário, 
ou seja, realizar a interação do operador do caixa com o sistema, mas, em algumas situações, seria possível.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Service import cliente_service
from util import *

def incluir_cliente():
    nome = entrar_nome()
    try:
        cliente_service.incluir_cliente(nome)
        print("Cliente incluido")
    except Exception as ex:
        print(ex)

def consultar_clientes():
    try:
        clientes = cliente_service.consultar_clientes()
        for cliente in clientes:
            print(cliente)
    except Exception as ex:
        print(ex)

def consultar_cliente():
    id = entrar_id()
    try:
        cliente = cliente_service.consultar_cliente(id)
        return cliente
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)


def alterar_cliente():
    id = entrar_id()
    nome = entrar_nome()
    try:
        cliente_service.alterar_cliente(id, nome)
        print("Cliente alterado")
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

def excluir_cliente():
    id = entrar_id()
    try:
        cliente_service.excluir_cliente(id)
        print("Cliente excluido")
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

#print(consultar_cliente())
#incluir_cliente()