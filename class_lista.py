# Classe para representar uma lista de compras

class ListaDeCompras:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item, quantidade):
        item = item.strip().lower()
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser um número positivo.")
        if item in self.itens:
            self.itens[item] += quantidade
        else:
            self.itens[item] = quantidade

    def remover_quantidade(self, item, quantidade):
        item = item.strip().lower()
        if item not in self.itens:
            raise KeyError("Item não encontrado na lista.")
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser um número positivo.")
        if quantidade >= self.itens[item]:
            del self.itens[item]
        else:
            self.itens[item] -= quantidade

    def marcar_comprado(self, item):
        item = item.strip().lower()
        if item in self.itens:
            del self.itens[item]
        else:
            raise KeyError("Item não encontrado na lista.")

    def listar_itens(self):
        return self.itens