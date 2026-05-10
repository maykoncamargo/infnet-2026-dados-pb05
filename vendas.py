from tabulate import tabulate
from datetime import date, datetime
from util import *

vendas = []


def criar_venda(lista):
    id = criar_id(lista)
    nome = f'Cliente {id}'
    data = data_atual()
    hora = hora_atual()
    return[nome, data, hora, []]


def adicionar_produto(venda, produto, qtd, preco):
    id = criar_id(venda[3])
    total = int(qtd) * int(preco)
    venda[3].append([id, produto, qtd, preco, total])



def imprimir_nf(venda):                     # usar Docstring para gear relatório
    cliente = venda[0]
    data = venda[1]
    hora = venda[2]
    lista_compras = venda[3]

    valor_total = 0
    qtd_itens = 0

    print(cliente)
    print(f'Data: {data} {hora}')
    print()

    print(tabulate(lista_compras, headers=['Item', "Produto", "Quant.", "Preço", "Total"]))

    for i in lista_compras:
        valor_total = valor_total + i[4]   # coluna total
        qtd_itens = qtd_itens + 1

    print()
    print(f'Itens: {qtd_itens}')
    print(f'Total: {valor_total}')


def fechamento_caixa(vendas):
    fechamento = []
    for venda in vendas:
        cliente = venda[0]
        total = sum(item[3] for item in venda[3])
        fechamento.append([cliente,total])
    return fechamento


def relatório_de_fechamento_caixa(vendas):
    data = data_atual()
    hora = hora_atual()
    print('Fechamento do Caixa')
    print(f'Data: {data} {hora}')

    fechamento_clientes = fechamento_caixa(vendas) 
    
    print()
    print(tabulate(fechamento_clientes, headers=['Cliente', "Total"]))
    print()
    total_vendas = sum(total[1] for total in fechamento_clientes)
    print(f'Total de Vendas:  {total_vendas}\n')
