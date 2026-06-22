import streamlit as st

from controllers.analisador_controller import (
    listar_historico_por_aluno,
    processar_e_salvar_texto,
)
from controllers.cadastro_controller import cadastrar_aluno, listar_alunos


def exibir_analise(analise):
    st.subheader("Resultado da analise")
    st.write(f"Nivel estimado: {analise.nivel_estimado}")

    st.subheader("Indicadores linguisticos")

    for indicador in analise.indicadores:
        with st.expander(f"{indicador.tipo}: {indicador.quantidade}"):
            if indicador.itens:
                st.write(", ".join(indicador.itens))
            else:
                st.write("Este indicador nao possui lista de itens.")

    st.subheader("Pontos fortes")

    if analise.pontos_fortes:
        for ponto in analise.pontos_fortes:
            st.write(f"- {ponto}")
    else:
        st.write("Nenhum ponto forte identificado.")

    st.subheader("Lacunas")

    if analise.lacunas:
        for lacuna in analise.lacunas:
            st.write(f"- {lacuna}")
    else:
        st.write("Nenhuma lacuna identificada.")


def exibir_historico(aluno_id):
    st.subheader("Histórico de análises do aluno")

    historico = listar_historico_por_aluno(aluno_id)

    if not historico:
        st.write("Este aluno ainda não possui análises salvas.")
        return

    for item in historico:
        titulo = f"Análise {item['id']} - {item['data_analise']}"
        with st.expander(titulo):
            st.write(f"**Data da análise:** {item['data_analise']}")
            st.write(f"**Total de palavras:** {item['total_palavras']}")
            st.write(f"**Substantivos:** {item['substantivos']}")
            st.write(f"**Verbos:** {item['verbos']}")
            st.write(f"**Adjetivos:** {item['adjetivos']}")
            st.write(f"**Advérbios:** {item['adverbios']}")
            st.write(f"**Conectores:** {item['conectores']}")
            if item["feedback"]:
                st.write("**Feedback:**")
                st.write(item["feedback"])


def executar_interface():
    st.title("Plataforma de Proficiencia em Alemao")

    aba_cadastro, aba_analise = st.tabs(["Cadastro de Aluno", "Analise Linguistica"])

    with aba_cadastro:
        st.header("Cadastro de Aluno")

        nome = st.text_input("Nome completo do aluno:")
        nivel = st.selectbox("Nivel atual:", ["A1", "A2", "B1", "B2"], key="nivel_cadastro")
        motivo = st.text_area("Motivo para estudar alemao:")
        interesses = st.text_area("Interesses / hobbies:")
        outros_idiomas = st.text_input("Outros idiomas que fala:")
        observacoes = st.text_area("Observacoes:")

        if st.button("Cadastrar aluno"):
            if nome.strip() == "":
                st.warning("Digite o nome do aluno.")
            else:
                aluno = cadastrar_aluno(
                    nome=nome,
                    nivel_atual=nivel,
                    motivo_estudo=motivo,
                    interesses=interesses,
                    outros_idiomas=outros_idiomas,
                    observacoes=observacoes,
                )
                st.success(f"Aluno {aluno.nome} cadastrado com sucesso!")

        st.subheader("Alunos cadastrados")

        alunos = listar_alunos()

        if alunos:
            for aluno in alunos:
                with st.expander(f"{aluno.id_aluno} - {aluno.nome} ({aluno.nivel_atual})"):
                    ficha = aluno.exibir_ficha()
                    for chave, valor in ficha.items():
                        st.write(f"**{chave}:** {valor}")
        else:
            st.write("Nenhum aluno cadastrado ainda.")

    with aba_analise:
        st.header("Analise Linguistica")

        alunos = listar_alunos()

        if alunos:
            nomes_alunos = [aluno.nome for aluno in alunos]

            nome_escolhido = st.selectbox("Escolha o aluno:", nomes_alunos)

            aluno_selecionado = next(
                aluno for aluno in alunos
                if aluno.nome == nome_escolhido
            )

            st.write(f"Nivel atual: {aluno_selecionado.nivel_atual}")

            texto = st.text_area("Digite uma producao em alemao:")

            if st.button("Analisar e salvar transcricao"):
                if texto.strip() == "":
                    st.warning("Digite uma transcricao antes de analisar.")
                else:
                    analise, transcricao_id = processar_e_salvar_texto(
                        aluno_id=aluno_selecionado.id_aluno,
                        texto=texto,
                    )

                    st.success(f"Transcricao {transcricao_id} salva com sucesso.")

                    st.subheader("Dados do aluno")
                    st.write(f"Nome: {aluno_selecionado.nome}")
                    st.write(f"Nivel atual informado: {aluno_selecionado.nivel_atual}")

                    exibir_analise(analise)

            exibir_historico(aluno_selecionado.id_aluno)

        else:
            st.warning("Cadastre um aluno antes de realizar a analise.")
