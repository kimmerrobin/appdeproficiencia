class Aluno:
    def __init__(
        self,
        id_aluno: int,
        nome: str,
        nivel_atual: str,
        motivo_estudo: str = "",
        interesses: str = "",
        outros_idiomas: str = "",
        observacoes: str = "",
        data_inicio: str = ""
    ):
        self.id_aluno = id_aluno
        self.nome = nome
        self.nivel_atual = nivel_atual
        self.motivo_estudo = motivo_estudo
        self.interesses = interesses
        self.outros_idiomas = outros_idiomas
        self.observacoes = observacoes
        self.data_inicio = data_inicio
        self.total_producoes = 0
        self.historico = []

    def adicionar_analise(self, analise):
        self.historico.append(analise)
        self.total_producoes += 1

    def atualizar_nivel(self, novo_nivel: str):
        self.nivel_atual = novo_nivel

    def consultar_historico(self):
        return self.historico

    def exibir_ficha(self):
        return {
            "ID": self.id_aluno,
            "Nome": self.nome,
            "Nível atual": self.nivel_atual,
            "Motivo de estudo": self.motivo_estudo,
            "Interesses": self.interesses,
            "Outros idiomas": self.outros_idiomas,
            "Observações": self.observacoes,
            "Data de início": self.data_inicio,
            "Total de produções": self.total_producoes
        }

    def __str__(self):
        return f"{self.nome} - {self.nivel_atual}"