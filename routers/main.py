from controllers.main import index

def index_rotas(app):
    app.add_url_rule("/", endpoint="home", view_func=index, methods=['GET'])
