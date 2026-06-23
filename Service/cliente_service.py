"""
O arquivo cliente_service.py fará o tratamento das regras de negócios. 

Por exemplo, a consulta de um produto deverá tratar se o id é maior que zero e se o produto existe no banco de dados. 
Outro exemplo, na alteração de um produto, além das regras de negócios da consulta, também deverá verificar se a quantidade em estoque é suficiente para a venda. 
A camada de serviço deverá implementar todas as funcionalidades do CRUD de produtos, mesmo que o caixa não as utilize. 
Todos os erros decorrentes da camada de serviço deverão ser repassados para a camada superior de onde partiu a chamada para o serviço.
"""

from util import *

import Repository.cliente_repository as cliente_repository
from Models.clientes import Cliente


def incluir_cliente(nome):
    if not validar_nome(nome):
        raise ValueError("Erro: nome inválido")
    cliente = Cliente(None, nome)
    cliente_repository.incluir_cliente(cliente)


def consultar_clientes():
    cliente = cliente_repository.consultar_clientes()
    return cliente


def consultar_cliente(id):
    if not validar_id(id):
        raise ValueError(f"Erro: id do cliente {id} inválido")
    cliente = cliente_repository.consultar_cliente(id)
    if not cliente:
        raise ValueError(f"Erro: cliente {id} não encontrado")
    return cliente


def alterar_cliente(id, nome):
    if not validar_id(id):
        raise ValueError(f"Erro: id do cliente {id} inválido")
    if not validar_nome(nome):
        raise ValueError("Erro: nome inválido")
    cliente = cliente_repository.consultar_cliente(id)
    if not cliente:
        raise ValueError(f"Erro: cliente {id} não encontrado")
    cliente.nome = nome
    cliente_repository.alterar_cliente(id, cliente)


def excluir_cliente(id):
    if not validar_id(id):
        raise ValueError(f"Erro: id do cliente {id} inválido")
    cliente = cliente_repository.consultar_cliente(id)
    if not cliente:
        raise ValueError(f"Erro: cliente {id} não encontrado")
    cliente_repository.excluir_cliente(id)


#incluir_cliente("Coca-colaaaa")
#alterar_cliente(5, "Coca")
#print(consultar_cliente(5))
#excluir_cliente(5)
#print(consultar_clientes())