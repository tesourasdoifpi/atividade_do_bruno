from databases.sqlitedb import SQLiteDB

class PostagemDAO:
    def __init__(self):
        self.db = SQLiteDB()

    def criar_postagem(self, data: dict):
        """Cria uma nova postagem no banco de dados."""
        self.db.conectar()
        query = "INSERT INTO postagem (titulo, conteudo, usuario_id) VALUES (?, ?, ?)"
        titulo = data.get('titulo')
        conteudo = data.get('conteudo')
        usuario_id = data.get('usuario_id')
        params = (titulo, conteudo, usuario_id)
        result = self.db.executar(query, params)
        self.db.desconectar()
        return result


    def listar_postagens(self):
        """Lista todas as postagens com seus respectivos autores."""
        self.db.conectar()

        query = """
            SELECT
                postagem.id,
                postagem.titulo,
                postagem.conteudo,
                postagem.usuario_id,
                usuario.username AS autor
            FROM postagem
            INNER JOIN usuario
                ON postagem.usuario_id = usuario.id
            ORDER BY postagem.id DESC
        """

        result = self.db.consultar(query)

        self.db.desconectar()

        postagens = []

        if result:
            for row in result:
                postagem = {
                    'id': row['id'],
                    'titulo': row['titulo'],
                    'conteudo': row['conteudo'],
                    'usuario_id': row['usuario_id'],
                    'autor': row['autor']
                }

                postagens.append(postagem)

        return postagens

    def pegar_postagem_por_id(self, postagem_id: int):
        """Captura os dados de uma postagem pelo ID."""

        self.db.conectar()

        try:
            query = """
                SELECT
                    p.id,
                    p.titulo,
                    p.conteudo,
                    p.usuario_id,
                    u.username AS autor
                FROM postagem AS p
                INNER JOIN usuario AS u
                    ON p.usuario_id = u.id
                WHERE p.id = ?
            """

            params = (postagem_id,)

            result = self.db.consultar(query, params)

            if result:
                row = result[0]

                postagem = {
                    'id': row['id'],
                    'titulo': row['titulo'],
                    'conteudo': row['conteudo'],
                    'usuario_id': row['usuario_id'],
                    'autor': row['autor']
                }

                return postagem

            return None

        finally:
            self.db.desconectar()

    def pegar_postagem_por_titulo(self, titulo: str):
        """Captura os dados de uma postagem pelo título."""
        self.db.conectar()
        query = "SELECT * FROM postagem WHERE titulo = ?"
        params = (titulo,)
        result = self.db.consultar(query, params)
        self.db.desconectar()
        if result:
            row = result[0]
            postagem = {
                'id': row['id'],
                'titulo': row['titulo'],
                'conteudo': row['conteudo'],
                'usuario_id': row['usuario_id']
            }
            return postagem
        return None

    def listar_postagens_por_usuario(self, usuario_id: int):
        """Lista todas as postagens de um usuário específico."""
        self.db.conectar()
        query = "SELECT * FROM postagem WHERE usuario_id = ? ORDER BY id DESC"
        params = (usuario_id,)
        result = self.db.consultar(query, params)
        self.db.desconectar()
        postagens = []
        if result:
            for row in result:
                postagem = {
                    'id': row['id'],
                    'titulo': row['titulo'],
                    'conteudo': row['conteudo'],
                    'usuario_id': row['usuario_id']
                }
                postagens.append(postagem)
        return postagens

    