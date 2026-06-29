from services.analisador import analisar_transcricao
from database import analise_repository, transcricao_repository

def processar_texto(texto: str):
    return analisar_transcricao(texto)


def _buscar_quantidade(analise, termo):
    termo = termo.lower()
    for indicador in analise.indicadores:
        if termo in indicador.tipo.lower():
            return indicador.quantidade
    return None


def _montar_feedback(analise):
    partes = [f"Nivel estimado: {analise.nivel_estimado}"]

    if analise.pontos_fortes:
        partes.append("Pontos fortes: " + "; ".join(analise.pontos_fortes))

    if analise.lacunas:
        partes.append("Lacunas: " + "; ".join(analise.lacunas))

    return "\n".join(partes)


def processar_e_salvar_texto(aluno_id: int, texto: str):
    analise = analisar_transcricao(texto)
    transcricao_id = transcricao_repository.salvar_transcricao(aluno_id, texto)
    analise_id = analise_repository.salvar_analise(
        transcricao_id=transcricao_id,
        total_palavras=_buscar_quantidade(analise, "total"),
        substantivos=_buscar_quantidade(analise, "substant"),
        verbos=_buscar_quantidade(analise, "verbo"),
        adjetivos=_buscar_quantidade(analise, "adjet"),
        adverbios=_buscar_quantidade(analise, "adv"),
        conectores=_buscar_quantidade(analise, "conjun"),
        feedback=_montar_feedback(analise)
    )

    analise.id_analise = analise_id
    return analise, transcricao_id


def listar_historico_por_aluno(aluno_id: int):
    return analise_repository.listar_analises_por_aluno(aluno_id)


def deletar_analise(analise_id: int):
    return analise_repository.deletar_analise(analise_id)
