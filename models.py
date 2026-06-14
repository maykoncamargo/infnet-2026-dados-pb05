
class Produto:

    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.id},{self.nome},{self.quantidade},{self.preco}"
    
    #permite imprimir o valor do objeto instanciado em listas
    def __repr__(self):
        return self.__str__()
    
    