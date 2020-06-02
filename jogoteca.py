from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__) #__name__ it's the package name
app.secret_key = "cryptasecret"

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route("/") #defining a route for the function
def index():
    return render_template("lista.html", titulo ="Jogos", jogos = lista)


jogo1 = Jogo("Super Mario", "Plataforma", "Snes")
jogo2 = Jogo("Pkm red", "Rpg", "Gameboy")
jogo3 = Jogo("MK", "Luta", "SNES")
lista = [jogo1, jogo2, jogo3]

@app.route('/novo')
def novo():
    return render_template("novo.html", titulo = "Novo Jogo")

@app.route("/criar", methods =["POST", ] )
def criar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return redirect('/')


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/autenticar", methods=["POST"])
def autentiar():
    if "mestra" == request.form['senha']:
        session['usuario_logado'] = request.form["usuario"]
        flash(request.form["usuario"] + " logou com sucesso")
        return redirect("/")
    else:
        flash("Não logado, tente novamente")
        return redirect("/login")

@app.route("/logout")
def logout():
    session["usuario_logado"] = None
    flash("Nenhum usuário logado")
    return redirect("/")

app.run(debug = True)
