class IndicadorLinguistico:
    def __init__(self, tipo: str, quantidade: int, itens=None, percentual: float = 0):
        self.tipo = tipo
        self.quantidade = quantidade
        self.itens = itens if itens is not None else []
        self.percentual = percentual

    def atualizar_quantidade(self, nova_quantidade: int):
        self.quantidade = nova_quantidade

    def atualizar_percentual(self, novo_percentual: float):
        self.percentual = novo_percentual

    def exibir(self):
        return {
            "tipo": self.tipo,
            "quantidade": self.quantidade,
            "itens": self.itens,
            "percentual": self.percentual
        }