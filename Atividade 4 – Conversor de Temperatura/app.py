from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return 'Conversor de Temperatura - É possível acessar /celsius/valor para converter para Fahrenheit ou /fahrenheit/valor para converter para Celsius.'

@app.route('/celsius/<int:temp>')
def celsius(temp):
    fahrenheit = (temp * 9/5) + 32
    return f'{temp} é igual a {fahrenheit:.2f}'

@app.route('/fahrenheit/<int:temp>')
def fahrenheit(temp):
    celsius = (temp - 32) * 5/9
    return f'{temp} é igual a {celsius:.2f}'

if __name__ == '__main__':
    app.run()
