"""
O arquivo produto_repository.py fará as funções de acesso ao banco de dados, 
ou seja, o CRUD completo propriamente dito. 
Os possíveis erros nessa camada devem ser repassados e tratadas pelas camadas superiores.

""" 
from conectar_db import *
from models import Produto


def incluir_produto(produto):
    query = "insert into produtos (nome, quantidade, preco) values (?, ?, ?);"

    conn = connect()
    try:
        cursor = conn.cursor()
        dados = (produto.nome, produto.quantidade, produto.preco)
        cursor.execute(query, dados)
        conn.commit()
    except Exception as ex:
        raise Exception(f"Erro: {ex}")
    finally:
        disconnect(conn)

def consultar_produtos():
    query = "SELECT * FROM produtos;"

    produtos = []
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        registros = cursor.fetchall()
        for registro in registros:
            produto = Produto(registro[0], registro[1], registro[2], registro[3])
            produtos.append(produto)
    except Exception as ex:
        raise Exception(f"Erro: {ex}")
    finally:
        disconnect(conn)
    return produtos
    
def consultar_produto(id):
    query = "SELECT * FROM produtos WHERE id = ?;"

    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute(query, (id,))
        registro = cursor.fetchone()
        if registro:
            return Produto(registro[0], registro[1], registro[2], registro[3])
        return None
    except Exception as ex:
        raise Exception(f"Erro: {ex}")
    finally:
        disconnect(conn)

def alterar_produto(id, produto):
    query = "UPDATE produtos SET nome = ?, quantidade = ?, preco = ? WHERE id = ?;"

    conn = connect()
    try:
        cursor = conn.cursor()
        dados = (produto.nome, produto.quantidade, produto.preco, id)
        cursor.execute(query, dados)
        conn.commit()
    except Exception as ex:
        raise Exception(f"Erro: {ex}")
    finally:
        disconnect(conn)

def excluir_produto(id):
    query = "DELETE FROM produtos WHERE id = ?;"

    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute(query, (id,))
        conn.commit()
    except Exception as ex:
        raise Exception(f"Erro: {ex}")
    finally:
        disconnect(conn)



#p = Produto(id= None, nome="Coca-cola", preco=10.0, quantidade=100)
#incluir_produto(p)
#print(consultar_produtos())
#print(consultar_produto(1))
#alterar_produto(2,p)
#excluir_produto(1)
#print(consultar_produtos())

