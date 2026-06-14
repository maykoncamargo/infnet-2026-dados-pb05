import util
import produto_service
import produto_cliente
import pandas as pd

def criar_pedido(vendas):
    id = util.criar_id(vendas)
    cliente = f'Cliente {id}'
    data = util.data_atual()
    hora = util.hora_atual()
    itens = []
    return {'cliente': cliente, 'data': data, 'hora': hora, 'itens': itens}

def item_pedido(itens):              
    id_venda = util.criar_id(itens)
    id_produto = util.entrar_item_vendido()
    quantidade_vendida = util.entrar_quantidade()
    return {
        'id_venda': id_venda,
        'id_produto': id_produto,
        'quantidade_vendida': quantidade_vendida
    }

def itens_pedido():
    itens = []                        
    while True:
        itens.append(item_pedido(itens))
        if not util.entrar_continuar():
            break
    return itens 

def entrar_item_vendido():
    while True:
        try:
            id = util.entrar_inteiro("ID do produto: ")
            produto = produto_service.consultar_produto(id)
            return produto.id
        except Exception as erro:
            print("ERRO: Um erro inesperado aconteceu", erro)


def dataFrame_produtos():
    dados = produto_service.consultar_produtos()
    df = pd.DataFrame([{
        'ID': p.id,
        'Nome': p.nome,
        'Quantidade': p.quantidade,
        'Preço': p.preco
    } for p in dados])
    return  df


def dataFrame_pedido(pedido):
    df = pd.DataFrame([{
        'Cliente': pedido['cliente'],
        'Data':    pedido['data'],
        'Hora':    pedido['hora']
    }])
    return df

def dataFrame_itens_pedido(itens_pedido):
    df = pd.DataFrame([{
        'ID Venda':           item['id_venda'],
        'ID Produto':         item['id_produto'],
        'Quantidade Vendida': item['quantidade_vendida']
    } for item in itens_pedido])
    return df


def nota_fiscal(pedido, itens_pedido):
    produtos_df = dataFrame_produtos()
    itens_df = dataFrame_itens_pedido(itens_pedido)  # ← recebe lista

    cabecalho = f"Cliente: {pedido['cliente']} | Data: {pedido['data']} | Hora: {pedido['hora']}"
    print('='*50)
    print(cabecalho)
    print('='*50)

    df_p = pd.merge(itens_df, produtos_df, left_on='ID Produto', right_on='ID')
    df_p['Total'] = df_p['Quantidade Vendida'] * df_p['Preço']

    print(df_p[['ID Venda', 'Nome', 'Quantidade Vendida', 'Preço', 'Total']].to_string(index=False))

    valor_total = df_p['Total'].sum()
    qtd_itens = df_p['Quantidade Vendida'].sum()
    print('='*50)
    print(f'Itens:  {qtd_itens}')
    print(f'Total:  R$ {valor_total:.2f}')
    print('='*50)


def nota_fiscal_agrupada(pedido, itens_pedido):
    produtos_df = dataFrame_produtos()
    itens_df = dataFrame_itens_pedido(itens_pedido)

    cabecalho = f"Cliente: {pedido['cliente']} | Data: {pedido['data']} | Hora: {pedido['hora']}"
    print('='*50)
    print(cabecalho)
    print('='*50)

    # Merge e cálculo
    df_p = pd.merge(itens_df, produtos_df, left_on='ID Produto', right_on='ID')
    df_p['Total'] = df_p['Quantidade Vendida'] * df_p['Preço']

    # Agrupamento por Nome do produto
    df_agrupado = df_p.groupby('Nome').agg(
        Quantidade=('Quantidade Vendida', 'sum'),
        Preço=('Preço', 'first'),
        Total=('Total', 'sum')
    ).reset_index()

    print(df_agrupado[['Nome', 'Quantidade', 'Preço', 'Total']].to_string(index=False))

    valor_total = df_agrupado['Total'].sum()
    qtd_itens = df_agrupado['Quantidade'].sum()
    print('='*50)
    print(f'Itens:  {qtd_itens}')
    print(f'Total:  R$ {valor_total:.2f}')
    print('='*50)

def fechamento_caixa(vendas):
    rows = []
    for venda in vendas:
        produtos_df = dataFrame_produtos()
        itens_df = dataFrame_itens_pedido(venda['itens'])

        df_p = pd.merge(itens_df, produtos_df, left_on='ID Produto', right_on='ID')
        df_p['Total'] = df_p['Quantidade Vendida'] * df_p['Preço']

        rows.append({
            'Cliente': venda['cliente'],
            'Data':    venda['data'],
            'Hora':    venda['hora'],
            'Itens':   df_p['Quantidade Vendida'].sum(),
            'Total':   df_p['Total'].sum()
        })

    df_fechamento = pd.DataFrame(rows)
    return df_fechamento


def relatorio_fechamento_caixa(vendas):
    df = fechamento_caixa(vendas)

    print('='*50)
    print(f'Fechamento do Caixa — {util.data_atual()} {util.hora_atual()}')
    print('='*50)
    print(df.to_string(index=False))
    print('='*50)
    print(f'Total de Vendas:  R$ {df["Total"].sum():.2f}')
    print(f'Total de Itens:   {int(df["Itens"].sum())}')
    print('='*50)

