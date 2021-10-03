from flask import Flask, render_template, request, redirect, session, flash
from funcionario import Funcionario

app = Flask(__name__)

app.secret_key = 'SISTEMAFINANCEIRO'

@app.route('/')
def index():
    return render_template('login.html',
                           titulo = "Login")

@app.route('/menu')
def menu():
    return render_template('menu.html')


if __name__ == '__main__':
    app.run(debug = True)





