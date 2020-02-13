from flask import Flask
import translator

app = Flask(__name__)

@app.route('/')
def index():
    return 'Página inicial'

@app.route('/<int(signed=True):number>')
def getExtenso(number):
    if number > -100000 and number < 100000:
        return {
            'success'   : True,
            'extenso': translator.translate(number)
        }
    else:
        return {
            'success'   : False,
            'msg'       : 'Número digitado está fora do intervalo [-99999, 99999]'
        }


@app.errorhandler(404)
def not_found(e):
    return "<h1>Página não encontrada : 404</h1><br><h3>A página que você está procurando pode ter sido removida, teve seu nome alterado ou está temporariamente indisponível.</h3>"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
