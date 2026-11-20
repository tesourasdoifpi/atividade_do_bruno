from flask import Flask
from databases.sqlitedb import SQLiteDB
from routers.main import index_rotas
from routers.usuario_routes import usuario_rotas
from routers.postagem_routes import postagem_rotas

app = Flask(__name__)
app.secret_key = "de87988da4caa7adcffe28f0533a79a3fda9a0dd58c48825" 

db = SQLiteDB()
db.conectar()
db.executar_script_sql('databases/scripts/criar_tabela.sql')

index_rotas(app)
usuario_rotas(app)
postagem_rotas(app)