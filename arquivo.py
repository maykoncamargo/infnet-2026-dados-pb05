import os.path
from models import Produto

ARQ = 'produtos.csv'
DIR = os.path.dirname(os.path.abspath(__file__)) # ler aquivo onde esta executando o programa
ARQ = os.path.join(DIR, ARQ)


#read
def ler_estoque() ->list:
    estoque = []
    try:
        with open(file=ARQ, mode="r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                campo = linha.split(",")
                id = int(campo[0])
                nome = str(campo[1]) 
                est = int(campo[2]) 
                preco = float(campo[3])
                estoque.append(Produto(id,nome, est, preco))
    except Exception as erro:
        print("ERRO: Erro ao abrir o arquivo", erro)
        exit
    return estoque


# write one line and of file
def gravar_estoque(estoques:list):
    try:
        with open(ARQ, mode='w', encoding= "UTF-8") as arquivo:
            for produto in estoques:
                linha = f"{produto.id},{produto.nome},{produto.estoque},{produto.preco}\n"
                arquivo.write(linha)
    except Exception as ex:
        print("ERRO: gravação do Arquivo", ex)
        exit()


#estoque = ler_estoque()
#print(estoque)