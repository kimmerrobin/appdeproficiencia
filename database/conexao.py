import os

import psycopg2
import streamlit as st


def obter_database_url():
    try:
        database_url = st.secrets["DATABASE_URL"]
    except Exception:
        database_url = None

    if not database_url:
        database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError(
            "DATABASE_URL nao foi configurada. Defina em st.secrets['DATABASE_URL'] "
            "ou na variavel de ambiente DATABASE_URL."
        )

    return database_url


def conectar():
    return psycopg2.connect(obter_database_url())
