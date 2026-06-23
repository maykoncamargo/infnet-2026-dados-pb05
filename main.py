import Dados.banco as banco
from estoque import *
from vendas import *
from util import *
from Crud import produto_crud

def iniciar_banco_de_dados():
    banco.limpar_tabelas()
    banco.criar_banco()
    banco.carregar_dados()

def criar_caixa():
    vendas = []
    return vendas

def abrir_caixa(vendas):               
    opcao = menu_inicar()
    match opcao:
        case "1": iniciar_atendimento(vendas)
        case "2": fechar_caixa(vendas)
        case _: print("opcao Inválida")

def iniciar_atendimento(vendas):
    print("Iniciando Atendimento ao Cliente: ")
    pedido = criar_pedido(vendas)
    itens = itens_pedido()   
    pedido['itens'] = itens
    nota_fiscal_agrupada(pedido, itens)
    vendas.append(pedido)
    print("Atendimento finalizado com sucesso!\n")
    abrir_caixa(vendas)

def fechar_caixa(vendas):
    relatorio_fechamento_caixa(vendas)
    relatorio_produtos_sem_estoque(vendas)
    atualizar_estoque(vendas)

if __name__ == "__main__":
    iniciar_banco_de_dados()
    produto_crud.consultar_produtos()
    vendas = criar_caixa()
    abrir_caixa(vendas)