from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return 'Contador de Caracteres de um Texto Passado na URL.'

@app.route('/contar/<texto>')
def contador(texto):
    quantidade = len(texto)
    return f"{texto} tem {quantidade} caracteres"


if __name__ == '__main__':
    app.run()
