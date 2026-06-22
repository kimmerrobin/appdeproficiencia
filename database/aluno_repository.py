from psycopg2.extras import RealDictCursor

from database.conexao import conectar


def salvar_aluno(nome, nivel_inicial=None, observacoes=None):
    conexao = conectar()
    try:
        with conexao:
            with conexao.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    """
                    INSERT INTO alunos (nome, nivel_inicial, observacoes)
                    VALUES (%s, %s, %s)
                    RETURNING id
                    """,
                    (nome, nivel_inicial, observacoes),
                )
                return cursor.fetchone()["id"]
    finally:
        conexao.close()


def listar_alunos():
    conexao = conectar()
    try:
        with conexao.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT id, nome, nivel_inicial, observacoes, data_cadastro
                FROM alunos
                ORDER BY data_cadastro DESC, id DESC
                """
            )
            return [dict(aluno) for aluno in cursor.fetchall()]
    finally:
        conexao.close()


def buscar_aluno_por_id(aluno_id):
    conexao = conectar()
    try:
        with conexao.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT id, nome, nivel_inicial, observacoes, data_cadastro
                FROM alunos
                WHERE id = %s
                """,
                (aluno_id,),
            )
            aluno = cursor.fetchone()
            return dict(aluno) if aluno else None
    finally:
        conexao.close()
