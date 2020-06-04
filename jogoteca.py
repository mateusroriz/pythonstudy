from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__) #__name__ it's the package name
app.secret_key = "cryptasecret"

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

usuario1 = Usuario('ciclano', "Ciclano", '1234')
usuario2 = Usuario("fulano", "Fulano Ciclano", "js")
usuario3 = Usuario("deltrano", "Deltrano", "python")

usuarios = {usuario1.id: usuario1, usuario2.id: usuario2, usuario3.id: usuario3}

jogo1 = Jogo("Super Mario", "Plataforma", "Snes")
jogo2 = Jogo("Pkm red", "Rpg", "Gameboy")
jogo3 = Jogo("MK", "Luta", "SNES")
lista = [jogo1, jogo2, jogo3]

@app.route("/") #defining a route for the function
def index():
    return render_template("lista.html", titulo ="Jogos", jogos = lista)

@app.route('/novo')
def novo():
    if "usuario_logado" not in session or session["usuario_logado"] == None:
        return redirect(url_for("login", proxima=url_for("novo"))) #novo é o caminho a seguir depois de dar login
    return render_template("novo.html", titulo = "Novo Jogo")

@app.route("/criar", methods =["POST", ] )
def criar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return redirect(url_for("index"))


@app.route("/login")
def login():
    proxima = request.args.get("proxima")
    return render_template("login.html", proxima = proxima ) #jogando informação pro formulario


@app.route("/autenticar", methods=["POST"])
def autenticar():
    if request.form["usuario"] in usuarios:
        usuario = usuarios[request.form["usuario"]]
        if usuario.senha == request.form["senha"]:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + " logou com sucesso")
            proxima_pagina = request.form["proxima"]
            return redirect(proxima_pagina)
    else:
        flash("Não logado, tente novamente")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session["usuario_logado"] = None
    flash("Nenhum usuário logado")
    return redirect(url_for("index"))

app.run(debug = True)
