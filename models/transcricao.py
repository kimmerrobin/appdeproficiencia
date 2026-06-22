class Transcricao:
    def __init__(self, id_transcricao: int, texto: str, data: str = "", idioma: str = "alemao"):
        self.id_transcricao = id_transcricao
        self.texto = texto
        self.data = data
        self.idioma = idioma

    def salvar(self):
        return {
            "id_transcricao": self.id_transcricao,
            "texto": self.texto,
            "data": self.data,
            "idioma": self.idioma
        }

    def editar(self, novo_texto: str):
        self.texto = novo_texto