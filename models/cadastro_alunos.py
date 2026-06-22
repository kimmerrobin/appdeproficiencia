class CadastroAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        return self.alunos

    def buscar_por_nome(self, nome):
        for aluno in self.alunos:
            if aluno.nome.lower() == nome.lower():
                return aluno
        return None

    def quantidade_alunos(self):
        return len(self.alunos)