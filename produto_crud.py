"""
O arquivo produto_crud.py é um arquivo que permitirá às operações de CRUD na tabela de produtos do banco de dados. 
A ideia é permitir que o administrador do sistema faça alguma correção necessária na tabela de produtos. 
O seu programa não é obrigado a utilizar esse arquivo como a camada de interface com o usuário, 
ou seja, realizar a interação do operador do caixa com o sistema, mas, em algumas situações, seria possível.
"""

import produto_service
from util import *

def incluir_produto():
    nome = entrar_nome_produto()
    quantidade = entrar_quantidade()
    preco = entrar_preco()
    try:
        produto_service.incluir_produto(nome, quantidade, preco)
        print("Produto incluido")
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

def consultar_produtos():
    try:
        produtos = produto_service.consultar_produtos()
        for produto in produtos:
            print(produto)
    except Exception as ex:
        print(ex)

def alterar_produto():
    id = entrar_id()
    nome = entrar_nome_produto()
    quantidade = entrar_quantidade()
    preco = entrar_preco()
    try:
        produto_service.alterar_produto(id, nome, quantidade, preco)
        print("Produto alterado")
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

def excluir_produto():
    id = entrar_id()
    try:
        produto_service.excluir_produto(id)
        print("Produto excluido")
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

