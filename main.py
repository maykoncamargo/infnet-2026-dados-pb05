from tabulate import tabulate 
from estoque import *
from vendas import *
from util import *
from arquivo import *


def abrir_caixa(estoque, vendas):               
    opcao = menu_inicar()
    match opcao:
        case "1": iniciar_atendimento(estoque,vendas)
        case "2": fechar_caixa(estoque, vendas)
        case _: print("opcao Inválida")
    

def entrar_item_vendido():
    valores_validos = [1,2,3,4,5]
    while True:
        try:
            codigo_item = input("Código Item ou S para sair:")
            print(codigo_item)
            if codigo_item.lower() == "s":
                return codigo_item
            
            if int(codigo_item) in valores_validos or codigo_item.lower=="s":
                return codigo_item
            
            print("ERRO: Código Inválido")

        except Exception as erro:
            print("ERRO: Um erro inesperado aconteceu", erro)


def entrar_quantidade_vendida():
        while True:
            try:
                qtd = (input("Quantidade: "))
                if qtd.isdigit() or int(qtd) >= 0:
                    return int(qtd)
                print('ERRO: Quantidade deve ser maior que zero.')
            except Exception as erro:
                print("ERRO: Um erro inesperado aconteceu", erro)


def iniciar_atendimento(estoque, vendas):
    venda = criar_venda(vendas)             # Cria o local on vai ficar a venda

    item = 0    
    while item != "s":
        item  = entrar_item_vendido()
        if item.lower() == "s":
            break

        qtd = entrar_quantidade_vendida()
        print()
        produto = procurar_nome_produto(int(item), estoque)
        preco = procurar_preço_produto(int(item), estoque)

        adicionar_produto(venda, produto, qtd, preco)
    
    imprimir_nf(venda)
    vendas.append(venda)
    print()

    abrir_caixa(estoque, vendas)


def fechar_caixa(estoque, vendas):
    relatório_de_fechamento_caixa(vendas)
    relatório_produtos_sem_estoque(estoque, vendas)
    atualizar_estoque(estoque, vendas)


if __name__ == "__main__":
    estoque = ler_estoque()
    abrir_caixa(estoque, vendas)