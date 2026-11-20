

class Postagem:
    def __init__(self, data: dict):
        self.data = data
        self.errors = []

    def validate(self):
        titulo = self.data.get('titulo')
        conteudo = self.data.get('conteudo')
        autor = self.data.get('usuario_id')

        if not titulo or not conteudo:
            self.errors.append("Título e conteúdo são obrigatórios.")

        if titulo and len(titulo) < 3:
            self.errors.append("O título deve ter pelo menos 3 caracteres.")

        if conteudo and len(conteudo) < 10:
            self.errors.append("O conteúdo deve ter pelo menos 10 caracteres.")

        if not autor:
            self.errors.append("O autor da postagem é obrigatório.")

        usuario_id = self.data.get('usuario_id')
        from models.usuario import Usuario
        usuario = Usuario(self.data)
        
        if not usuario.existe_usuario_por_id(usuario_id):
            self.errors.append("O usuário especificado não existe.")

        return len(self.errors) == 0

    def save(self):
        """Salva a postagem no banco de dados."""
        from dao.postagemDAO import PostagemDAO
        postagem_dao = PostagemDAO()
        result = postagem_dao.criar_postagem(self.data)
        return result

    def detalhar_postagem(id:int):
        from dao.postagemDAO import PostagemDAO
        postagem_dao = PostagemDAO()
        return postagem_dao.pegar_postagem_por_id(id)

    def listar_postagens():
        """Lista todas as postagens no banco de dados."""
        from dao.postagemDAO import PostagemDAO
        postagem_dao = PostagemDAO()
        return postagem_dao.listar_postagens()

    def listar_postagens_por_usuario(self, usuario_id:int):
        """Lista todas as postagens de um usuário específico no banco de dados."""
        from dao.postagemDAO import PostagemDAO
        postagem_dao = PostagemDAO()
        return postagem_dao.listar_postagens_por_usuario(usuario_id)

    @property
    def titulo(self):
        return self.data.get('titulo', '')

    @property
    def conteudo(self):
        return self.data.get('conteudo', '')

    @property
    def autor(self):
        return self.data.get('usuario_id', None)