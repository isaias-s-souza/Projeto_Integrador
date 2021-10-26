import pyodbc
import configparser
from flask import Flask, render_template, request, redirect, session, flash

from dao import ContaExtratoDao, FuncionarioDao, FornecedorDao
from models import Funcionario, ContaExtrato, Fornecedor

app = Flask(__name__)
app.secret_key = 'SISTEMAFINANCEIRO'

config = configparser.ConfigParser()
config.read('CONFIGURACAO.ini')

DB = pyodbc.connect('Driver={SQL Server};' +
                      'Server=' + config['CONFIGURACAO_GERAL']['DATABASE'] + ';' +
                      'Database=SISTEMA_FINANCEIRO;' +
                      'UID=sa;' +
                      'PWD=2021financesys;' +
                      'Trusted_Connection=no;')

conta_extrato_dao   = ContaExtratoDao(DB)
funcionario_dao     = FuncionarioDao(DB)
fornecedor_dao      = FornecedorDao(DB)



@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=')
    else:
        return render_template('menu.html')

@app.route('/conta_extrato')
def conta_extrato():
    lista = conta_extrato_dao.listar()

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=')
    else:
        return render_template('conta_extrato.html', contas=lista)

@app.route('/criar_conta_extrato', methods = ['POST', ])
def criar_conta_extrato():
    nome            = request.form['nome']
    descricao       = request.form['descricao']
    agencia         = request.form['agencia']
    conta           = request.form['conta']
    saldo_inicial   = request.form['saldo_inicial']

    nova_conta_extrato = ContaExtrato(nome, descricao, agencia, conta, saldo_inicial, True)

    conta_extrato_dao.salvar(nova_conta_extrato)
    lista = conta_extrato_dao.listar()

    return render_template('conta_extrato.html', contas=lista)

@app.route('/funcionario')
def funcionario():
    lista = funcionario_dao.listar()
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=')
    else:
        return render_template('funcionario.html', funcionarios=lista)


@app.route('/criar_funcionario', methods = ['POST', ])
def criar_funcioario():
    nome            = request.form['nome']
    endereco        = request.form['endereco']
    cpf             = request.form['cpf']
    cnpj            = request.form['cnpj']
    login           = request.form['login']
    novo_funcionario = Funcionario(nome=nome, cliente=False, fornecedor=False, funcionario=True, endereco=endereco,
                                   cpf=cpf, cnpj=cnpj, login=login, ativo=True, telefone='', celular='', email='',
                                   datacadastro='')

    funcionario_dao.salvar(novo_funcionario)
    lista = funcionario_dao.listar()
    return render_template('funcionario.html', funcionarios=lista)


@app.route('/fornecedor')
def fornecedor():
    lista = fornecedor_dao.listar()
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=')
    else:
        return render_template('fornecedor.html', fornecedores=lista)


@app.route('/criar_fornecedor', methods=['POST', ])
def criar_fornecedor():
    nome            = request.form['nome']
    razaosocial     = request.form['razaosocial']
    endereco        = request.form['endereco']
    cpf             = request.form['cpf']
    cnpj            = request.form['cnpj']
    #self, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo, telefone,
    #celular, email, datacadastro, razaosocial, codigo=None
    novo_fornecedor = Fornecedor(nome=nome, cliente=False, fornecedor=True, funcionario=False,
                                 endereco=endereco, cpf=cpf, cnpj=cnpj, ativo=True, telefone='',
                                 celular='', email='', datacadastro='',razaosocial=razaosocial)

    fornecedor_dao.salvar(novo_fornecedor)
    lista = fornecedor_dao.listar()
    return render_template('fornecedor.html', fornecedores=lista)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = ''

    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods = ['POST', ])
def autenticar():
    funcionario = funcionario_dao.busca_por_id(request.form['usuario'])

    if funcionario:
        if funcionario.get_senha() == request.form['senha']:
            session['usuario_logado'] = request.form['usuario']
            session['codigo_logado']  = funcionario.get_codigo()
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



