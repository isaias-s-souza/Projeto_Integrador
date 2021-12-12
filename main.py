import pyodbc
import configparser
from flask import Flask, render_template, request, redirect, session, flash

from dao import ContaExtratoDao, FuncionarioDao, FornecedorDao, ClienteDao, LancamentoDao
from models import Cliente, Funcionario, ContaExtrato, Fornecedor, Lancamento

app = Flask(__name__)
app.secret_key = 'SISTEMAFINANCEIRO'

config = configparser.ConfigParser()
config.read('CONFIGURACAO.ini')

DB = pyodbc.connect('Driver={SQL Server};' +
                      'Server=' + config['CONFIGURACAO_GERAL']['SERVIDOR'] + ';' +
                      'Database=' + config['CONFIGURACAO_GERAL']['BANCODEDADOS'] + ';' +
                      'UID=' + config['CONFIGURACAO_GERAL']['USUARIO'] + ';' +
                      'PWD=' + config['CONFIGURACAO_GERAL']['SENHA'] + ';' +
                      config['CONFIGURACAO_GERAL']['MODOENCRYPT'] + 
                      'Trusted_Connection=no;' + 
                      'Connection Timeout=30;')

conta_extrato_dao   = ContaExtratoDao(DB)
funcionario_dao     = FuncionarioDao(DB)
fornecedor_dao      = FornecedorDao(DB)
cliente_dao         = ClienteDao(DB)  
lancamento_dao      = LancamentoDao(DB)            


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
    conta           = request.form['numero-conta']
    saldo_inicial   = request.form['saldo-inicial']

    nova_conta_extrato = ContaExtrato(nome, descricao, agencia, conta, saldo_inicial, True)

    conta_extrato_dao.salvar(nova_conta_extrato)
    lista = conta_extrato_dao.listar()
    return render_template('conta_extrato.html', contas=lista)


@app.route('/alterar_conta_extrato', methods=['POST', ])
def alterar_conta_extrato():
    id              = request.form['id-alteracao']
    nome            = request.form['nome-alteracao']
    descricao       = request.form['descricao-alteracao']
    agencia         = request.form['agencia-alteracao']
    numero_conta    = request.form['numero-conta-alteracao']
    saldo_inicial   = request.form['saldo-inicial-alteracao']
    if request.form.get('ativo-alteracao') == None:
        ativo = False
    else:
        ativo = True

    conta_extrato_editada = ContaExtrato(nome=nome, descricao=descricao, agencia=agencia, 
                                         numero_conta=numero_conta, saldo_inicial=saldo_inicial, 
                                         ativo=ativo, codigo=id)

    conta_extrato_dao.salvar(conta_extrato_editada)
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
    telefone        = request.form['telefone']
    celular         = request.form['celular']
    email           = request.form['email']
    cpf             = request.form['cpf']
    login           = request.form['login']

    novo_funcionario = Funcionario(nome=nome, cliente=False, fornecedor=False, funcionario=True, endereco=endereco,
                                   cpf=cpf, cnpj='', login=login, ativo=True, telefone=telefone, celular=celular, 
                                   email=email, datacadastro='', codigo='')

    funcionario_dao.salvar(novo_funcionario)
    lista = funcionario_dao.listar()
    return render_template('funcionario.html', funcionarios=lista)

@app.route('/alterar_funcionario', methods=['POST', ])
def alterar_funcionario():
    id          = request.form['id-alteracao']
    nome        = request.form['nome-alteracao']
    endereco    = request.form['endereco-alteracao']
    telefone    = request.form['telefone-alteracao']
    celular     = request.form['celular-alteracao']
    email       = request.form['email-alteracao']
    cpf         = request.form['cpf-alteracao']
    login       = request.form['login-alteracao']

    if request.form.get('ativo-alteracao') == None:
        ativo = False
    else:
        ativo = True
    
    funcionario_editado = Funcionario(nome=nome, cliente=False, fornecedor=False, funcionario=True, endereco=endereco,
                                   cpf=cpf, cnpj='', login=login, ativo=ativo, telefone=telefone, celular=celular, 
                                   email=email, datacadastro='', codigo=id)
    funcionario_dao.salvar(funcionario_editado)
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
    telefone        = request.form['telefone']
    celular         = request.form['celular']
    email           = request.form['email']
    cpf             = request.form['cpf']
    cnpj            = request.form['cnpj']
    #self, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo, telefone,
    #celular, email, datacadastro, razaosocial, codigo=None
    novo_fornecedor = Fornecedor(nome=nome, cliente=False, fornecedor=True, funcionario=False,
                                 endereco=endereco, cpf=cpf, cnpj=cnpj, ativo=True, telefone=telefone,
                                 celular=celular, email=email, datacadastro='', razaosocial=razaosocial)

    fornecedor_dao.salvar(novo_fornecedor)
    lista = fornecedor_dao.listar()
    return render_template('fornecedor.html', fornecedores=lista)

@app.route('/alterar_fornecedor', methods=['POST', ])
def alterar_fornecedor():
    id          = request.form['id-alteracao']
    nome        = request.form['nome-alteracao']
    razaosocial = request.form['razaosocial-alteracao']
    endereco    = request.form['endereco-alteracao']
    telefone    = request.form['telefone-alteracao']
    celular     = request.form['celular-alteracao']
    email       = request.form['email-alteracao']
    cpf         = request.form['cpf-alteracao']
    cnpj        = request.form['cnpj-alteracao']

    if request.form.get('ativo-alteracao') == None:
        ativo = False
    else:
        ativo = True
    # nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo, telefone,
    #celular, email, datacadastro, razaosocial, codigo=None
    fornecedor_editado = Fornecedor(nome=nome, cliente=False, fornecedor=True, funcionario=False, endereco=endereco,
                                   cpf=cpf, cnpj=cnpj, ativo=ativo, telefone=telefone, celular=celular, 
                                   email=email, datacadastro='', razaosocial=razaosocial, codigo=id)
    fornecedor_dao.salvar(fornecedor_editado)
    lista = fornecedor_dao.listar()
    return render_template('fornecedor.html', fornecedores=lista)


#CLIENTE
@app.route('/cliente')
def cliente():
    lista = cliente_dao.listar()
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=')
    else:
        return render_template('cliente.html', clientes=lista)


@app.route('/criar_cliente', methods=['POST', ])
def criar_cliente():
    nome            = request.form['nome']
    endereco        = request.form['endereco']
    telefone        = request.form['telefone']
    celular         = request.form['celular']
    email           = request.form['email']
    cpf             = request.form['cpf']
    cnpj            = request.form['cnpj']
    #nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo, telefone,
    #celular, email, datacadastro, codigo=None
    novo_cliente = Cliente(nome=nome, cliente=True, fornecedor=False, funcionario=False,
                                 endereco=endereco, cpf=cpf, cnpj=cnpj, ativo=True, telefone=telefone,
                                 celular=celular, email=email, datacadastro='')

    cliente_dao.salvar(novo_cliente)
    lista = cliente_dao.listar()

    return render_template('cliente.html', clientes=lista)     

@app.route('/alterar_cliente', methods=['POST', ])
def alterar_cliente():
    id          = request.form['id-alteracao']
    nome        = request.form['nome-alteracao']
    endereco    = request.form['endereco-alteracao']
    telefone    = request.form['telefone-alteracao']
    celular     = request.form['celular-alteracao']
    email       = request.form['email-alteracao']
    cpf         = request.form['cpf-alteracao']
    cnpj        = request.form['cnpj-alteracao']

    if request.form.get('ativo-alteracao') == None:
        ativo = False
    else:
        ativo = True
    #nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo, telefone,
    #celular, email, datacadastro, codigo=None
    cliente_editado = Cliente(nome=nome, cliente=True, fornecedor=False, funcionario=False, endereco=endereco,
                              cpf=cpf, cnpj=cnpj, ativo=ativo, telefone=telefone, celular=celular, 
                              email=email, datacadastro='', codigo=id)
    cliente_dao.salvar(cliente_editado)
    lista = cliente_dao.listar()
    return render_template('cliente.html', clientes=lista)

#CONTA A PAGAR
@app.route('/conta_a_pagar', methods=['POST','GET' ])
def conta_a_pagar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=')
    else:
        condPagts = lancamento_dao.listar()
        relacaoCondPagtsCodLancamento = list()
        for descricao in condPagts:
            relacaoCondPagtsCodLancamento.append({'CONDICAO_PAGTO.COD_CONDICAO_PAGTO' : str(descricao.cod_cond_pagamento), 'CONDICAO_PAGTO.PARCELA' : descricao.parcela})

        return render_template('conta_a_pagar.html', relacaoCondPagts=relacaoCondPagtsCodLancamento)


@app.route('/criar_conta_a_pagar', methods=['POST','GET' ])
def criar_conta_a_pagar():

    
    fornecedor              = request.form['fornecedor']
    valor                   = request.form['valor']
    documento               = request.form['documento']
    historico_observacao    = request.form['historico_observacao']
    cond_pagts              = request.form['cond_pagts']
    parcela                 = request.form['parcela']
    data_emissao            = request.form['data_emissao']
    data_vencimento         = request.form['data_vencimento']
    cod_subcategoria        = request.form['cod_subcategoria']

    nova_conta_a_pagar = Lancamento(valor=valor, documento=documento, historico_observacao=historico_observacao,
                                    cod_cond_pagamento=cond_pagts, parcela=parcela,data_emissao=data_emissao,
                                    data_vencimento=data_vencimento,cod_subcategoria=cod_subcategoria,cod_pessoa=fornecedor)
    
    lancamento_dao.salvar(nova_conta_a_pagar)
    lista = lancamento_dao.listar()

    return render_template('conta_a_pagar.html', relacaoCondPagts=lista)


#CONTA A RECEBER
@app.route('/conta_a_receber')
def conta_a_receber():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=')
    else:
        return render_template('conta_a_receber.html')

@app.route('/extrato_bancario')
def extrato_bancario():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=')
    else:
        contas = conta_extrato_dao.listar()
        #Tranforma em uma lista no seguinte padrão NOME CONTA - COD BANCO
        relacaoNomeCodConta= list()
        for conta in contas:
            relacaoNomeCodConta.append({'DESCRICAO' : conta.get_nome() + ' - ' + str(conta.get_codigo()), 'CODIGO': str(conta.get_codigo())})

        return render_template('extrato_bancario.html', relacaoContasConsulta=relacaoNomeCodConta)

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
            flash('Senha Inválida, tente novamente!')
            return redirect('/login')    
    else:
        flash('Usuário não cadastro, tente novamente!')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug = True)



