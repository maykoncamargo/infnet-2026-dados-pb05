"""
O arquivo produto_cliente.py terá a responsabilidade de testar todas as funcionalidades da camada de serviço 
sem precisar passar pela camada de interface com o usuário, 

ou seja, pelo código do arquivo produto_crud.py.
"""
import Service.produto_service as produto_service

def incluir_produto():
    try:
        produto_service.incluir_produto(nome, quantidade, preco)
    except ValueError as ex:
        print(f"Erro: {ex}")
    except Exception as ex:
        print(f"Erro: {ex}")
        
def consultar_produtos():
    try:
        produtos = produto_service.consultar_produtos()
        for produto in produtos:
            print(produto)
    except Exception as ex:
        print(f"Erro: {ex}")

def consultar_produto():
    try:
        produto = produto_service.consultar_produto(id)
        return produto
    except ValueError as ex:
        print(f"Erro: {ex}")
    except Exception as ex:
        print(f"Erro: {ex}")

def alterar_produto():
    try:
        produto_service.alterar_produto(id, nome, quantidade, preco)
    except ValueError as ex:
        print(f"Erro: {ex}")
    except Exception as ex:
        print(f"Erro: {ex}")

def excluir_produto():
    try:
        produto_service.excluir_produto(id)
    except ValueError as ex:
        print(f"Erro: {ex}")
    except Exception as ex:
        print(f"Erro: {ex}")