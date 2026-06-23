from Crud import cliente_crud
from Service import cliente_service

def entrar_cliente():
    opcao = menu_cliente()
    cliente = None
    match opcao:
        case "1": cliente = cliente_crud.consultar_cliente()
        case "2": cliente = cadastrar_cliente()
        case _: print("opcao Inválida")
    return cliente

def menu_cliente():
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

def cadastrar_cliente():
    cliente_crud.incluir_cliente()
    cliente = cliente_service.consultar_clientes()
    print(cliente)
    return cliente[-1]


#print(menu_cliente())
#print(entrar_cliente())
#print(cadastrar_cliente())