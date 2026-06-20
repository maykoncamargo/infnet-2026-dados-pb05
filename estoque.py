from vendas import *
import Service.produto_service as produto_service


def relatorio_produtos_sem_estoque(vendas):
    # DataFrame de produtos do banco
    produtos_df = dataFrame_produtos()

    # Consolidar todos os itens vendidos
    rows = []
    for venda in vendas:
        itens_df = dataFrame_itens_pedido(venda['itens'])
        rows.append(itens_df)

    if not rows:
        print("Nenhuma venda registrada.")
        return

    # Unir todos os itens em um único DataFrame
    todos_itens_df = pd.concat(rows, ignore_index=True)

    # Total vendido por produto
    vendidos_df = todos_itens_df.groupby('ID Produto').agg(
        Vendido=('Quantidade Vendida', 'sum')
    ).reset_index()

    # Merge com produtos
    df = pd.merge(produtos_df, vendidos_df, left_on='ID', right_on='ID Produto', how='left')
    df['Vendido'] = df['Vendido'].fillna(0)

    # Saldo de estoque
    df['Saldo'] = df['Quantidade'] - df['Vendido']

    # Filtrar sem estoque
    df_sem_estoque = df[df['Saldo'] <= 0][['Nome', 'Quantidade', 'Vendido', 'Saldo']]

    # Relatório
    print('='*50)
    print('Produtos sem Estoque')
    print('='*50)
    if df_sem_estoque.empty:
        print("Nenhum produto sem estoque.")
    else:
        print(df_sem_estoque.to_string(index=False))
    print('='*50)


def atualizar_estoque(vendas):
    produtos_df = dataFrame_produtos()

    rows = []
    for venda in vendas:
        itens_df = dataFrame_itens_pedido(venda['itens'])
        rows.append(itens_df)

    if not rows:
        print("Nenhuma venda registrada.")
        return

    todos_itens_df = pd.concat(rows, ignore_index=True)

    vendidos_df = todos_itens_df.groupby('ID Produto').agg(
        Vendido=('Quantidade Vendida', 'sum')
    ).reset_index()

    df = pd.merge(produtos_df, vendidos_df, left_on='ID', right_on='ID Produto', how='left')
    df['Vendido'] = df['Vendido'].fillna(0)
    df['Nova Quantidade'] = df['Quantidade'] - df['Vendido']

    for _, row in df.iterrows():             # ← indentado dentro da função
        produto = Service.produto_service.consultar_produto(int(row['ID']))
        Service.produto_service.alterar_produto(
            int(row['ID']),
            produto.nome,
            int(row['Nova Quantidade']),
            produto.preco
        )

    print("Estoque atualizado com sucesso!") # ← indentado dentro da função