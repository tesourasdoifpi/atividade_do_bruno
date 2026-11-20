from flask import render_template, redirect, url_for, request, session
from models.usuario import Usuario


def cadastro():
    if request.method == 'GET':
        return render_template("usuario/cadastro.html")
    elif request.method == 'POST':
        data = {
            'username': request.form.get('username'),
            'senha': request.form.get('senha')
        }
        novo_usuario = Usuario(data)
        if novo_usuario.validate():
            result = novo_usuario.save()
            if result:
                return redirect(url_for('home'))
            else:
                return render_template("usuario/cadastro.html", error="Erro ao salvar o usuário.")
        else:
            return render_template("usuario/cadastro.html", errors=novo_usuario.errors)
            

def login():
    if request.method == 'GET':
        return render_template("usuario/login.html")
    elif request.method == 'POST':
        username = request.form.get('username')
        senha = request.form.get('senha')
        data = {
            'username': username,
            'senha': senha
        }
        usuario = Usuario(data)
        if usuario.usuario_existe_no_banco():
            if usuario.conferir_senha():
                session['username'] = username
                session['usuario_id'] = usuario.pegar_id_por_username(username)
                print(f"Usuário logado: {session['username']}, ID: {session['usuario_id']}")
                print(f"O tipo de session['usuario_id'] é: {type(session['usuario_id'])}")
                return redirect(url_for('home'))

            else:
                return render_template("usuario/login.html", errors=["Senha incorreta."])

        return render_template("usuario/login.html", errors=["Usuário não encontrado."])
    

def logout():
    session.pop('username', None)
    session.pop('usuario_id', None)
    return redirect(url_for('home'))