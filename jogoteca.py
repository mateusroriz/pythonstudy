from flask import Flask, render_template

app = Flask(__name__) #__name__ it's the package name

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route("/inicio") #defining a route for the function
def ola():
    jogo1 = Jogo("Super Mario", "Plataforma", "Snes")
    jogo2 = Jogo("Pkm red", "Rpg", "Gameboy")
    jogo3 = Jogo("MK", "Luta", "SNES")
    lista = [jogo1, jogo2, jogo3]
    return render_template("lista.html", titulo ="Jogos", jogos = lista)

app.run()
