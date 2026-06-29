from models.aluno import Aluno
from database import aluno_repository


def _montar_aluno(registro):
    if not registro:
        return None

    return Aluno(
        id_aluno=registro["id"],
        nome=registro["nome"],
        nivel_atual=registro["nivel_inicial"] or "",
        observacoes=registro["observacoes"] or "",
        data_inicio=str(registro["data_cadastro"] or "")
    )


def cadastrar_aluno(
    nome: str,
    nivel_atual: str,
    motivo_estudo: str = "",
    interesses: str = "",
    outros_idiomas: str = "",
    observacoes: str = "",
    data_inicio: str = ""
):
    id_aluno = aluno_repository.salvar_aluno(
        nome=nome,
        nivel_inicial=nivel_atual,
        observacoes=observacoes
    )

    return Aluno(
        id_aluno=id_aluno,
        nome=nome,
        nivel_atual=nivel_atual,
        motivo_estudo=motivo_estudo,
        interesses=interesses,
        outros_idiomas=outros_idiomas,
        observacoes=observacoes,
        data_inicio=data_inicio
    )


def listar_alunos():
    return [
        _montar_aluno(registro)
        for registro in aluno_repository.listar_alunos()
    ]


def buscar_aluno_por_nome(nome: str):
    for aluno in listar_alunos():
        if aluno.nome.lower() == nome.lower():
            return aluno
    return None


def deletar_aluno(aluno_id: int):
    return aluno_repository.deletar_aluno(aluno_id)
