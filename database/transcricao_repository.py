from psycopg2.extras import RealDictCursor

from database.conexao import conectar


def salvar_transcricao(aluno_id, texto):
    conexao = conectar()
    try:
        with conexao:
            with conexao.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    """
                    INSERT INTO transcricoes (aluno_id, texto)
                    VALUES (%s, %s)
                    RETURNING id
                    """,
                    (aluno_id, texto),
                )
                return cursor.fetchone()["id"]
    finally:
        conexao.close()


def listar_transcricoes_por_aluno(aluno_id):
    conexao = conectar()
    try:
        with conexao.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT id, aluno_id, texto, data_envio
                FROM transcricoes
                WHERE aluno_id = %s
                ORDER BY data_envio DESC, id DESC
                """,
                (aluno_id,),
            )
            return [dict(transcricao) for transcricao in cursor.fetchall()]
    finally:
        conexao.close()
