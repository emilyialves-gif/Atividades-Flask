from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return 'Tabuada Online da Emily - Você Pode Acessar a Tabuada de Qualquer Número Usando a URL'

@app.route('/tabuada/<int:n>')
def tabuada(n):
    resultado = f'Tabuada do {n} \n'
    for x in range(1, 11):
        resultado += f'{n} x {x} = {n * x} \n'
    return resultado

if __name__ == '__main__':
    app.run()
