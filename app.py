from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"Hello Flask"


@app.route("/versao")
def versao():
    versao = "1.1.0"
    return f"App v{versao}", 200

@app.route("/saudar/<nome>")
def saudar(nome):
    nome_formatado = nome.capitalize()
    return f"Olá, {nome_formatado}!", 200


