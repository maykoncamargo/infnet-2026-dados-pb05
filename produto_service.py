"""
O arquivo produto_service.py fará o tratamento das regras de negócios. 

Por exemplo, a consulta de um produto deverá tratar se o id é maior que zero e se o produto existe no banco de dados. 

Outro exemplo, na alteração de um produto, além das regras de negócios da consulta, também deverá verificar se a quantidade em estoque é suficiente para a venda. 

A camada de serviço deverá implementar todas as funcionalidades do CRUD de produtos, mesmo que o caixa não as utilize. 

Todos os erros decorrentes da camada de serviço deverão ser repassados para a camada superior de onde partiu a chamada para o serviço.


"""
import produto_repository
from Models.produto import Produto
from util import *

def incluir_produto(nome, quantidade, preco):
    if not validar_nome(nome):
        raise ValueError("Erro: nome inválido")
    if not validar_quantidade(quantidade):
        raise ValueError("Erro: quantidade inválida")
    if not validar_preco(preco):
        raise ValueError("Erro: preço inválido")
    produto = Produto(None, nome, quantidade, preco)
    produto_repository.incluir_produto(produto)

def consultar_produtos():
    produtos = produto_repository.consultar_produtos()
    return produtos

def consultar_produto(id):
    if not validar_id(id):
        raise ValueError(f"Erro: id do produto {id} inválido")
    produto = produto_repository.consultar_produto(id)
    if not produto:
        raise ValueError(f"Erro: produto {id} não encontrado")
    return produto


def alterar_produto(id, nome, quantidade, preco):
    if not validar_id(id):
        raise ValueError(f"Erro: id do produto {id} inválido")
    if not validar_nome(nome):
        raise ValueError("Erro: nome inválido")
    if not validar_quantidade(quantidade):
        raise ValueError("Erro: quantidade inválida")
    if not validar_preco(preco):
        raise ValueError("Erro: preço inválido")
    produto = produto_repository.consultar_produto(id)
    if not produto:
        raise ValueError(f"Erro: produto {id} não encontrado")
    produto.nome = nome
    produto.quantidade = quantidade
    produto.preco = preco
    produto_repository.alterar_produto(id, produto)

def excluir_produto(id):
    if not validar_id(id):
        raise ValueError(f"Erro: id do produto {id} inválido")
    produto = produto_repository.consultar_produto(id)
    if not produto:
        raise ValueError(f"Erro: produto {id} não encontrado")
    produto_repository.excluir_produto(id)




#incluir_produto("Coca-colaaaa", 10, 5.0)
#print(consultar_produtos())
#alterar_produto(5, "Coca", 20, 5.0)
#print(consultar_produto(5))
#excluir_produto(5)
#print(consultar_produtos())