from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return 'Par ou Ímpar - É possível acessar /parimpar/numero.'

@app.route('/parimpar/<int:numero>')
def parimpar(numero):
    if numero % 2 == 0:
        return f'{numero} é par.'
    else:
        return f'{numero} é ímpar.'

if __name__ == '__main__':
    app.run()
