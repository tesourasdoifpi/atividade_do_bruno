from flask import render_template, redirect, url_for, request, session
from models.postagem import Postagem

def minhas_postagens():
    if session['username']:
        postagens = Postagem.listar_postagens_por_usuario(session['usuario_id'])
        return render_template("postagem/minhas_postagens.html", postagens=postagens)
    return redirect(url_for('login'))


def nova_postagem():
    if session['username']:
        if request.method == 'GET':
            return render_template("postagem/nova_postagem.html")
        
        elif request.method == 'POST':
            data = {
                'titulo': request.form.get('titulo'),
                'conteudo': request.form.get('conteudo'),
                'usuario_id': session['usuario_id']
            }
            nova_postagem = Postagem(data)
            if nova_postagem.validate():
                result = nova_postagem.save()
                if result:
                    return redirect(url_for('feed'))
                else:
                    return render_template("postagem/nova_postagem.html", errors=["Erro ao salvar a postagem."])
            else:
                return render_template("postagem/nova_postagem.html", errors=nova_postagem.errors)
    return redirect(url_for('login'))

def feed():
    if not session['username']:
        return redirect(url_for('login'))
    postagens = Postagem.listar_postagens()
    return render_template("postagem/feed.html", postagens=postagens)


def detalhes_postagem(id):

    if not session.get('username'):
        return redirect(url_for('login'))

    postagem = Postagem.detalhar_postagem(id)

    if postagem:
        return render_template(
            "postagem/detalhes.html",
            postagem=postagem
        )

    return redirect(url_for('feed'))