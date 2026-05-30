from tabulate import tabulate 
from vendas import *
from arquivo import *
from models import Produto

ID = 0
NOME_PRODUTO = 1
QUANTIDADE = 2
PRECO_PRODUTO = 3

# usar constantes para valores
def procurar_preço_produto(id_estoque, lista):
    for produto in lista:
        if produto.id == id_estoque:
            return produto.preco
    print(f"Produto ID {id_estoque} não encontrado!")
    return None
        
def procurar_nome_produto(id_estoque, lista):
    for produto in lista:
        if produto.id == id_estoque:
            return produto.nome
    print(f"Produto ID {id_estoque} não encontrado!")
    return None

#estoque = ler_estoque()
#print(procurar_nome_produto(1, estoque))

def total_unidades_vendidas(vendas):
    resultado = []
    # intera sobre clientes
    for venda in vendas:
        #iterra na vendas
        for item in venda[3]:
            nome = item[NOME_PRODUTO]
            quantidade = item[QUANTIDADE]
            encontrado = False
            for r in resultado:
                if r[0] == nome:
                    r[1] += quantidade
                    encontrado = True
                    break
            if not encontrado:
                resultado.append([nome, quantidade])    
    return resultado
    


def relatório_produtos_sem_estoque(estoque, vendas):    
    unidades_vendidas = total_unidades_vendidas(vendas)
    resultado = []
    for produto in estoque:                                   
        nome = produto.nome
        quantidade_estoque = produto.estoque
        for vendido in unidades_vendidas:
            if vendido[0] == nome:
                saldo = int(quantidade_estoque) - int(vendido[1])
                if saldo <= 0:
                    resultado.append(nome)
    print('Produto sem estoque: ')
    for p in resultado:
        print(p)


def atualizar_estoque(estoque, vendas):
    produtos_vendidos = total_unidades_vendidas(vendas)
    for produto, qtd in produtos_vendidos:
        for p in estoque:
            if produto == p.nome:
                qtd_est = p.estoque
                qtd_vendido = qtd
                p.estoque =  int(qtd_est) - int(qtd_vendido)
    gravar_estoque(estoque)


"""
estoque = ler_estoque()
print(estoque)

vendas = [
    ['Cliente 1', '08/03/2026', '14:32:10', [
        [1, 'Produto 1', 1, 20.00],
        [2, 'Produto 2', 2, 40.00],
    ]],
    ['Cliente 2', '08/03/2026', '14:32:10', [
        [3, 'Produto 3', 3, 60.00],
        [4, 'Produto 4', 4, 80.00],
    ]],
    ['Cliente 3', '08/03/2026', '14:32:10', [
        [5, 'Produto 5', 5, 100.00],
        [1, 'Produto 1', 1, 30.00],
    ]],
]


#print(total_unidades_vendidas(vendas))

#est = atualizar_estoque(estoque, vendas)
#print(est)

#gravar_estoque(est)"""