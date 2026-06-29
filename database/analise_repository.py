from datetime import datetime, timezone

from psycopg2.extras import RealDictCursor

from database.conexao import conectar


def salvar_analise(
    transcricao_id,
    total_palavras=None,
    substantivos=None,
    verbos=None,
    adjetivos=None,
    adverbios=None,
    conectores=None,
    feedback=None,
):
    conexao = conectar()
    try:
        with conexao:
            with conexao.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    """
                    INSERT INTO analises (
                        transcricao_id,
                        total_palavras,
                        substantivos,
                        verbos,
                        adjetivos,
                        adverbios,
                        conectores,
                        feedback,
                        data_analise
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id
                    """,
                    (
                        transcricao_id,
                        total_palavras,
                        substantivos,
                        verbos,
                        adjetivos,
                        adverbios,
                        conectores,
                        feedback,
                        datetime.now(timezone.utc),
                    ),
                )
                return cursor.fetchone()["id"]
    finally:
        conexao.close()


def listar_analises_por_aluno(aluno_id):
    conexao = conectar()
    try:
        with conexao.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT
                    analises.id,
                    analises.transcricao_id,
                    transcricoes.aluno_id,
                    transcricoes.texto,
                    transcricoes.data_envio,
                    analises.total_palavras,
                    analises.substantivos,
                    analises.verbos,
                    analises.adjetivos,
                    analises.adverbios,
                    analises.conectores,
                    analises.feedback,
                    analises.data_analise
                FROM analises
                INNER JOIN transcricoes
                    ON transcricoes.id = analises.transcricao_id
                WHERE transcricoes.aluno_id = %s
                ORDER BY analises.data_analise ASC, analises.id ASC
                """,
                (aluno_id,),
            )
            return [dict(analise) for analise in cursor.fetchall()]
    finally:
        conexao.close()


def buscar_ultima_analise_por_aluno(aluno_id):
    conexao = conectar()
    try:
        with conexao.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT
                    analises.id,
                    analises.transcricao_id,
                    transcricoes.aluno_id,
                    transcricoes.texto,
                    transcricoes.data_envio,
                    analises.total_palavras,
                    analises.substantivos,
                    analises.verbos,
                    analises.adjetivos,
                    analises.adverbios,
                    analises.conectores,
                    analises.feedback,
                    analises.data_analise
                FROM analises
                INNER JOIN transcricoes
                    ON transcricoes.id = analises.transcricao_id
                WHERE transcricoes.aluno_id = %s
                ORDER BY analises.data_analise DESC, analises.id DESC
                LIMIT 1
                """,
                (aluno_id,),
            )
            analise = cursor.fetchone()
            return dict(analise) if analise else None
    finally:
        conexao.close()


def deletar_analise(analise_id):
    conexao = conectar()
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM analises
                    WHERE id = %s
                    """,
                    (analise_id,),
                )
                return cursor.rowcount > 0
    finally:
        conexao.close()
