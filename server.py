from flask import Flask
app = Flask(__name__)

def getExtenso(n):
    return n

@app.route('/')
def index():
    return 'Página inicial'

@app.route('/<number>')
def show_number(number):
    return {
        'extenso': getExtenso(number)
    }
