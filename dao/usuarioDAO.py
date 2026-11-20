from databases.sqlitedb import SQLiteDB

class UsuarioDAO:
    def __init__(self):
        self.db = SQLiteDB()

    def criar_usuario(self, data:dict):
        """Cria um novo usuário no banco de dados."""
        self.db.conectar()
        query = "INSERT INTO usuario (username, senha) VALUES (?, ?)"
        username = data.get('username')
        senha = data.get('senha')
        params = (username, senha)
        result = self.db.executar(query, params)
        self.db.desconectar()
        return result  

    def existe_usuario(self, username:str):
        """Verifica se um usuário já existe no banco de dados."""
        self.db.conectar()
        query = "SELECT * FROM usuario WHERE username = ?"
        params = (username,)
        result = self.db.consultar(query, params)
        self.db.desconectar()
        return len(result) > 0 if result else False

    def conferir_senha(self, data:dict):
        """Verifica se a senha fornecida corresponde à senha do usuário no banco de dados."""
        self.db.conectar()
        query = "SELECT * FROM usuario WHERE username = ? AND senha = ?"
        username = data.get('username')
        senha = data.get('senha')
        params = (username, senha)
        result = self.db.consultar(query, params)
        self.db.desconectar()
        return len(result) > 0 if result else False

    def existe_usuario_por_id(self, usuario_id:int):
        """Verifica se um usuário existe no banco de dados pelo ID."""
        self.db.conectar()
        query = "SELECT * FROM usuario WHERE id = ?"
        params = (usuario_id,)
        result = self.db.consultar(query, params)
        self.db.desconectar()
        return len(result) > 0 if result else False

    def capturar_usuario_por_id(self, usuario_id:int):
        """Captura os dados de um usuário pelo ID."""
        self.db.conectar()
        query = "SELECT * FROM usuario WHERE id = ?"
        params = (usuario_id,)
        result = self.db.consultar(query, params)
        self.db.desconectar()
        from ..models.usuario import Usuario
        for row in result:
            data = {                
                'username': row['username'],
                'senha': row['senha']
            }
        return Usuario(data)


    def capturar_username_por_id(self, usuario_id:int):
        """Captura o nome de usuário de um usuário pelo ID."""
        self.db.conectar()
        query = "SELECT username FROM usuario WHERE id = ?"
        params = (usuario_id,)
        result = self.db.consultar(query, params)
        self.db.desconectar()
        if result:
            return result[0]['username']
        return None

    def capturar_id_por_username(self, username:str):
        """Captura o ID de um usuário pelo nome de usuário."""
        self.db.conectar()
        query = "SELECT id FROM usuario WHERE username = ?"
        params = (username,)
        result = self.db.consultar(query, params)
        self.db.desconectar()
        if result:
            return result[0]['id']
        return None

    
        