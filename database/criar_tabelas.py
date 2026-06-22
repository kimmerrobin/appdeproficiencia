from database.conexao import conectar


def criar_tabelas():
    comandos = (
        """
        CREATE TABLE IF NOT EXISTS alunos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(150) NOT NULL,
            nivel_inicial VARCHAR(20),
            observacoes TEXT,
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS transcricoes (
            id SERIAL PRIMARY KEY,
            aluno_id INTEGER REFERENCES alunos(id) ON DELETE CASCADE,
            texto TEXT NOT NULL,
            data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS analises (
            id SERIAL PRIMARY KEY,
            transcricao_id INTEGER REFERENCES transcricoes(id) ON DELETE CASCADE,
            total_palavras INTEGER,
            substantivos INTEGER,
            verbos INTEGER,
            adjetivos INTEGER,
            adverbios INTEGER,
            conectores INTEGER,
            feedback TEXT,
            data_analise TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
    )

    conexao = conectar()
    try:
        with conexao:
            with conexao.cursor() as cursor:
                for comando in comandos:
                    cursor.execute(comando)
    finally:
        conexao.close()
