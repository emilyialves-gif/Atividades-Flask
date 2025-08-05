from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return 'Soma de Números - É possível acessar /soma/numero1/numero2 para somar dois números'

@app.route('/soma/<int:numero1>/<int:numero2>')
def soma(numero1,numero2):
    resultado = numero1 + numero2
    return f"A soma de {numero1} + {numero2} é {resultado}."


if __name__ == '__main__':
    app.run()