import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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


def entrar_id():
    while True:
        id = entrar_inteiro("Entre o id da conta: ")
        if id > 0:
            break
        else:
            print("Erro: id inválido")
    return id

def entrar_inteiro(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except:
            print("Erro: valor inválido")
    return num

def validar_nome(nome):
    return len(nome) >= 2

def validar_quantidade(quantidade):
    return quantidade >= 0

def validar_preco(preco):
    return preco >= 0

def validar_id(id):
    return id > 0 

def entrar_nome():
    while True:
        nome = input("Entrar o nome do cliente: ")
        nomes = nome.split(" ")
        if len(nomes) < 2:
            print("Erro: nome inválido")
        else:
            break
    return nome

def entrar_nome_produto():
    while True:
        nome = input("Entrar o nome do produto: ")
        if len(nome) < 2:
            print("Erro: nome inválido")
        else:
            break
    return nome

def entrar_preco():
    while True:
        preco = entrar_real("Entre com o preço do produto: ")
        if preco >= 0:
            break
        else:
            print("Erro: preço inválido")
    return preco

def entrar_quantidade():
    while True:
        quantidade = entrar_inteiro("Entre com a quantidade do produto: ")
        if quantidade >= 0:
            break
        else:
            print("Erro: quantidade inválida")
    return quantidade


def entrar_real(msg):
    while True:
        try:
            valor = float(input(msg))
            break
        except:
            print("Erro: dado inválido")
    return valor


def entrar_continuar():
    while True:
        resposta = input("Deseja adicionar outro item? (s/n): ").lower()
        if resposta in ['s', 'n']:
            return resposta == 's'
        print("Erro: resposta inválida. Digite 's' para sim ou 'n' para não.")