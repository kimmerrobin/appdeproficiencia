from models.indicador_linguistico import IndicadorLinguistico


class AnaliseLinguistica:
    def __init__(self, id_analise: int):
        self.id_analise = id_analise
        self.nivel_estimado = ""
        self.pontos_fortes = []
        self.lacunas = []
        self.indicadores = []

    def adicionar_indicador(self, indicador: IndicadorLinguistico):
        self.indicadores.append(indicador)

    def definir_nivel(self, nivel: str):
        self.nivel_estimado = nivel

    def adicionar_ponto_forte(self, ponto: str):
        self.pontos_fortes.append(ponto)

    def adicionar_lacuna(self, lacuna: str):
        self.lacunas.append(lacuna)

    def exibir_resultado(self):
        return {
            "nivel_estimado": self.nivel_estimado,
            "pontos_fortes": self.pontos_fortes,
            "lacunas": self.lacunas,
            "indicadores": [i.exibir() for i in self.indicadores]
            }