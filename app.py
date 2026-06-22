import streamlit as st

from database.criar_tabelas import criar_tabelas
from views.interface import executar_interface


def inicializar_banco():
    try:
        criar_tabelas()
    except RuntimeError as erro:
        st.warning(str(erro))
    except Exception as erro:
        st.error(f"Nao foi possivel inicializar o banco de dados: {erro}")


inicializar_banco()

executar_interface()

