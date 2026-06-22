import spacy
from collections import Counter

from models.analise_linguistica import AnaliseLinguistica
from models.indicador_linguistico import IndicadorLinguistico


nlp = spacy.load("de_core_news_sm")


def analisar_transcricao(texto: str) -> AnaliseLinguistica:
    doc = nlp(texto)

    analise = AnaliseLinguistica(id_analise=1)

    palavras_validas = [
        token for token in doc
        if not token.is_punct and not token.is_space
    ]

    total_palavras = len(palavras_validas)

    palavras_diferentes = sorted(list(set(
    token.lemma_.lower()
    for token in palavras_validas
)))

    verbos = [token.lemma_.lower() for token in palavras_validas if token.pos_ in ["VERB", "AUX"]]
    substantivos = [token.lemma_.lower() for token in palavras_validas if token.pos_ == "NOUN"]
    adjetivos = [token.lemma_.lower() for token in palavras_validas if token.pos_ == "ADJ"]
    adverbios = [token.lemma_.lower() for token in palavras_validas if token.pos_ == "ADV"]
    conjuncoes = [token.lemma_.lower() for token in palavras_validas if token.pos_ in ["CCONJ", "SCONJ"]]

    verbos_diferentes = sorted(list(set(verbos)))
    substantivos_diferentes = sorted(list(set(substantivos)))
    adjetivos_diferentes = sorted(list(set(adjetivos)))
    adverbios_diferentes = sorted(list(set(adverbios)))
    conjuncoes_diferentes = sorted(list(set(conjuncoes)))

    indicadores = [
        IndicadorLinguistico("Total de palavras", total_palavras),
        IndicadorLinguistico("Palavras diferentes", len(palavras_diferentes), palavras_diferentes),
        IndicadorLinguistico("Verbos diferentes", len(verbos_diferentes), verbos_diferentes),
        IndicadorLinguistico("Substantivos diferentes", len(substantivos_diferentes), substantivos_diferentes),
        IndicadorLinguistico("Adjetivos diferentes", len(adjetivos_diferentes), adjetivos_diferentes),
        IndicadorLinguistico("Advérbios diferentes", len(adverbios_diferentes), adverbios_diferentes),
        IndicadorLinguistico("Conjunções diferentes", len(conjuncoes_diferentes), conjuncoes_diferentes),
]

    for indicador in indicadores:
        analise.adicionar_indicador(indicador)

    definir_nivel_estimado(analise, total_palavras, verbos, substantivos, conjuncoes)
    gerar_feedback(analise, verbos, substantivos, conjuncoes, adjetivos)

    return analise


def definir_nivel_estimado(analise, total_palavras, verbos, substantivos, conjuncoes):
    if total_palavras >= 40 and len(set(verbos)) >= 5 and len(conjuncoes) >= 2:
        analise.definir_nivel("A2/B1")
    elif total_palavras >= 20 and len(set(verbos)) >= 3:
        analise.definir_nivel("A2")
    else:
        analise.definir_nivel("A1")


def gerar_feedback(analise, verbos, substantivos, conjuncoes, adjetivos):
    if len(set(verbos)) >= 4:
        analise.adicionar_ponto_forte("Boa variedade de verbos utilizados.")
    else:
        analise.adicionar_lacuna("Pouca variedade de verbos na produção.")

    if len(set(substantivos)) >= 5:
        analise.adicionar_ponto_forte("Boa presença de substantivos diferentes.")
    else:
        analise.adicionar_lacuna("Vocabulário nominal ainda limitado.")

    if len(set(conjuncoes)) >= 2:
        analise.adicionar_ponto_forte("Uso de conectores/conjunções na produção.")
    else:
        analise.adicionar_lacuna("Pouco uso de conectores e conjunções.")

    if len(adjetivos) == 0:
        analise.adicionar_lacuna("Não foram identificados adjetivos na produção.")