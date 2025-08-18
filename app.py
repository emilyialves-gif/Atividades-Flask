from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return 'Tabuada Online da Emily - Você Pode Acessar a Tabuada de Qualquer Número Usando a URL'

@app.route('/tabuada/<int:n>')
def tabuada(n):
    return (f'1 X {n} = {n*1}'
            f'2 X {n} = {n*2}'
            f'3 X {n} = {n*3}'
            f'4 X {n} = {n*4}'
            f'5 X {n} = {n*5}'
            f'6 X {n} = {n*6}'
            f'7 X {n} = {n*7}'
            f'8 X {n} = {n*8}'
            f'9 X {n} = {n*9}'
            f'10 X {n} = {n*10}')

if __name__ == '__main__':
    app.run()
