from Crud import cliente_crud
from Service import cliente_service

def entrar_cliente():
    opcao = menu_cliente()
    cliente = None
    match opcao:
        case "1": cliente = entrar_cliente_id()
        case "2": cliente = cadastrar_cliente()
        case _: print("opcao Inválida")
    return cliente


def menu_cliente():
    print("Clientes Cadastrados: ")
    print("ID, Cliente:")
    cliente_crud.consultar_clientes()
    print()
    print("========= CLIENTE =========")
    print('1 - Entrar com Id')
    print('2 - Cadastrar Cliente:')
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


def entrar_cliente_id():
    while True:
        try:
            cliente = cliente_crud.consultar_cliente()
            if cliente:
                return cliente
            print("ERRO: Opção Inválida, retornando ao menu de cliente...")
            menu_cliente()
        except Exception as erro:
            print(erro)
            print()

def cadastrar_cliente():
    print("Entrando em Cadastrar Cliente: ")
    cliente_crud.incluir_cliente()
    cliente = cliente_service.consultar_clientes()
    print(cliente)
    return cliente[-1]

#entrar_cliente()
#print(menu_cliente())
#print(entrar_cliente())
#print(cadastrar_cliente())