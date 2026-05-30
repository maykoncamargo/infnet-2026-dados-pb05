class Produto:
    def __init__(self, id, nome, estoque, preco):
        self.id = id
        self.nome = nome
        self.estoque = estoque
        self.preco = preco

    #permite imprimir o valor instanciado
    def __str__(self):
        return f"{self.id},{self.nome},{self.estoque},{self.preco}"
    
    #permite imprimir o valor do objeto instanciado em listas
    def __repr__(self):
        return self.__str__()
