from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "bienvenido al sistema"


@app.route("/saludo")
def saludo():
    return "hola aprendiz adso"


@app.route("/inventario")
def inventario():
    return "sistea inventario activo"


@app.route("/usuarios")
def usuarios():
    return "Sistema susuarios activo"


if __name__ == "__main__":
    app.run(debug=True, port=5001)

