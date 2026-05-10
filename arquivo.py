import os.path

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
                id_esoque = int(campo[0])
                produto = str(campo[1]) 
                qtd = int(campo[2]) 
                preco = int(campo[3])
                estoque.append({"id":id_esoque,"produto": produto, "qtd": qtd, "preco":preco})
    except Exception as erro:
        print("ERRO: Erro ao abrir o arquivo", erro)
        exit
    return estoque


# write one line and of file
def gravar_estoque(estoques:list):
    try:
        with open(ARQ, mode='w', encoding= "UTF-8") as arquivo:
            for item in estoques:
                linha = f"{item["id"]},{item['produto']},{item['qtd']},{item['preco']}\n"
                arquivo.write(linha)
    except Exception as ex:
        print("ERRO: gravação do Arquivo", ex)
        exit()

