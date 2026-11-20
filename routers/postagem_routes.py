from controllers.postagem_controller import minhas_postagens, nova_postagem, feed, detalhes_postagem

def postagem_rotas(app):
    app.add_url_rule("/minhas-postagens", endpoint="minhas_postagens", view_func=minhas_postagens, methods=['GET'])
    app.add_url_rule("/detalhar/<int:id>", endpoint="detalhes_postagem", view_func=detalhes_postagem, methods=['GET'])
    app.add_url_rule("/postagem", endpoint="postagem", view_func=nova_postagem, methods=['GET', 'POST'])
    app.add_url_rule("/feed", endpoint="feed", view_func=feed, methods=['GET'])