from controllers.usuario_controller import cadastro, login, logout

def usuario_rotas(app):
    app.add_url_rule("/login", endpoint="login", view_func=login, methods=['GET', 'POST'])
    app.add_url_rule("/cadastro", endpoint="cadastro", view_func=cadastro, methods=['GET', 'POST'])
    app.add_url_rule("/logout", endpoint="logout", view_func=logout, methods=['GET'])
