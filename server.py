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
            'extenso': translator.translate(number)
        }
    else:
        abort(401)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
