import pyodbc
from flask import Flask, render_template, request, redirect, session, flash

from dao import ContaExtratoDao, FuncionarioDao
from models import Funcionario, ContaExtrato

app = Flask(__name__)
app.secret_key = 'SISTEMAFINANCEIRO'

DB = pyodbc.connect('Driver={SQL Server};' +
                      'Server=DESKTOP-RRJIH9Q\SIS_FIN;' +
                      'Database=SISTEMA_FINANCEIRO;' +
                      'UID=sa;' +
                      'PWD=2021financesys;' +
                      'Trusted_Connection=no;')

conta_extrato_dao   = ContaExtratoDao(DB)
funcionario_dao     = FuncionarioDao(DB)

funcionario1 = Funcionario("Administrador", False, False, True, " ", " ", " ", "admin", "123", True, 1)
funcionario2 = Funcionario("Operador", False, False, True, " ", " ", " ", "op", "1234", True, 2)

funcionarios = {funcionario1.login:funcionario1, funcionario2.login:funcionario2}

@app.route('/')
def index():
    lista_conta       = conta_extrato_dao.listar()
    lista_funcionario = funcionario_dao.listar()
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=')
    else:
        return render_template('menu.html')

@app.route('/conta_extrato')
def conta_extrato():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=')
    else:
        return render_template('conta_extrato.html')


@app.route('/criar_conta_extrato', methods = ['POST', ])
def criar_conta_extrato():
    nome            = request.form['nome']
    descricao       = request.form['descricao']
    agencia         = request.form['agencia']
    conta           = request.form['conta']
    saldo_inicial   = request.form['saldo_inicial']

    nova_conta_extrato = ContaExtrato(nome, descricao, agencia, conta, saldo_inicial, True)

    conta_extrato_dao.salvar(nova_conta_extrato)

    return redirect('/')

@app.route('/funcionario')
def funcionario():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=')
    else:
        return render_template('funcionario.html')


@app.route('/criar_funcionario', methods = ['POST', ])
def criar_funcioario():
    nome            = request.form['nome']
    endereco        = request.form['endereco']
    cpf             = request.form['cpf']
    cnpj            = request.form['cnpj']
    novo_funcionario = Funcionario(nome, False, False, True, endereco, cpf, cnpj, nome.split()[0], "123", True)

    funcionario_dao.salvar(novo_funcionario)

    return redirect('/')

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
        print("Entrou!!")
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
    flash('Nenhum usuário logado')
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug = True)





