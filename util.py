from estoque import *
from vendas import *
from datetime import date, datetime


def menu_inicar():
    print("========= MENU =========")
    print('1 - Inicar Atendimento')
    print('2 - Fechar Caixa')
    print()
    valores_validos = ["1", "2"]
    while True:
        try:
            opcao = input("Entre com a opção: ")
            if opcao in valores_validos:
                return opcao
            print("ERRO: Opção Inválida")

        except Exception as erro:
            print("ERRO: opção inválida", erro)
            
def data_atual():
    return date.today().strftime("%d/%m/%Y")

def hora_atual():
    return datetime.now().strftime("%H:%M:%S")

def criar_id(lista):
    return len(lista)+1