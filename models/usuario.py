class Usuario:
    def __init__(self, data: dict):
        self.data = data
        self.errors = []

    def validate(self):
        """Valida os dados do usuário."""
        username = self.data.get('username')
        senha = self.data.get('senha')

        if not username or not senha:
            self.errors.append("Nome de usuário e senha são obrigatórios.")

        if username and senha:
            from dao.usuarioDAO import UsuarioDAO
            usuario_dao = UsuarioDAO()
            if usuario_dao.existe_usuario(username):
                self.errors.append("O nome de usuário já existe.")

        if not username or len(username) < 3:
            self.errors.append("O nome de usuário deve ter pelo menos 3 caracteres.")
        if not senha or len(senha) < 6:
            self.errors.append("A senha deve ter pelo menos 6 caracteres.")

        return len(self.errors) == 0

    def save(self):
        """Salva o usuário no banco de dados."""
        from dao.usuarioDAO import UsuarioDAO
        usuario_dao = UsuarioDAO()
        result = usuario_dao.criar_usuario(self.data)
        return result

    def usuario_existe_no_banco(self):
        """Verifica se o usuário foi cadastrado com sucesso."""
        from dao.usuarioDAO import UsuarioDAO
        usuario_dao = UsuarioDAO()
        username = self.data.get('username')
        return usuario_dao.existe_usuario(username)

    def conferir_senha(self):
        from dao.usuarioDAO import UsuarioDAO
        usuario_dao = UsuarioDAO()
        return usuario_dao.conferir_senha(self.data)

    def existe_usuario_por_id(self, usuario_id:int):
        """Verifica se um usuário existe no banco de dados pelo ID."""
        from dao.usuarioDAO import UsuarioDAO
        usuario_dao = UsuarioDAO()
        return usuario_dao.existe_usuario_por_id(usuario_id)

    def pegar_usuario_por_id(self, usuario_id:int):
        """Captura os dados de um usuário pelo ID."""
        from dao.usuarioDAO import UsuarioDAO
        usuario_dao = UsuarioDAO()
        return usuario_dao.capturar_usuario_por_id(usuario_id)

    def pegar_id_por_username(self, username:str):
        """Captura o ID de um usuário pelo nome de usuário."""
        from dao.usuarioDAO import UsuarioDAO
        usuario_dao = UsuarioDAO()
        return usuario_dao.capturar_id_por_username(username)

    @property
    def username(self):
        return self.data.get('username')
    

