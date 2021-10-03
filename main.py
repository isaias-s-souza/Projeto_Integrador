from flask import Flask, render_template, request, redirect, session, flash
from funcionario import Funcionario

app = Flask(__name__)
app.secret_key = 'SISTEMAFINANCEIRO'

funcionario1 = Funcionario(1, "Administrador", False, False, True, " ", " ", " ", "admin", "123")
funcionario2 = Funcionario(2, "Operador", False, False, True, " ", " ", " ", "op", "1234")

funcionarios = {funcionario1.login:funcionario1, funcionario2.login:funcionario2}

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=')
    else:
        return render_template('menu.html')


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = ''
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods =['POST', ])
def autenticar():
    if request.form['usuario'] in funcionarios:
        funcionario = funcionarios[request.form['usuario']]

        if funcionario.get_senha() == request.form['senha']:
            session['usuario_logado'] = request.form['usuario']
            flash(request.form['usuario'] + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']

            return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuário ou Senha Inválidos, insira os dados novamente!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado com sucesso!')
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug = True)





