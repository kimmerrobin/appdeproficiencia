from services.analisador import analisar_transcricao

texto = """
Ich gehe heute nach Hause.
Ich lerne Deutsch und arbeite als Lehrer.
Weil ich Deutsch liebe, schreibe ich jeden Tag.
"""

analise = analisar_transcricao(texto)

print(analise.exibir_resultado())
