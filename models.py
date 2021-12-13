class Pessoa:
    #Metódo construtor
    def __init__(self, codigo, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo,
                 telefone, celular, email, datacadastro):

        #Atributos Privados
        self.__codigo           = codigo
        self.__nome             = nome
        self.__endereco         = endereco
        self.__cpf              = cpf
        self.__cnpj             = cnpj
        self.__telefone         = telefone
        self.__celular          = celular
        self.__email            = email
        self.__datacadastro     = datacadastro
        self.__cliente          = cliente
        self.__fornecedor       = fornecedor
        self.__funcionario      = funcionario
        self.__ativo            = ativo

        #print("Cliente ", self.__nome, " cadastrado(a) com sucesso!")

    #Getters e Setters
    #CÓDIGO
    def get_codigo(self):
        return self.__codigo

    #NOME
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    #É CLIENTE
    def set_cliente(self, eh_cliente):
        self.__cliente = eh_cliente

    # É FORNECEDOR
    def set_fornecedor(self, eh_fornecedor):
        self.__fornecedor = eh_fornecedor

    # É FUNCIONÁRIO
    def set_funcionario(self, eh_funcionario):
        self.__funcionario = eh_funcionario

    #ENDEREÇO
    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    #CPF
    def get_cpf(self):
        return self.__cpf

    def set_cpf(self,cpf):
        self.__cpf = cpf
    #CNPJ
    def get_cnpj(self):
        return self.__cnpj

    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj

    #Definição de atributos da classe como propriedade

    @property
    def telefone(self):
        return self.__telefone
    @property
    def celular(self):
        return self.__celular
    @property
    def email(self):
        return self.__email
    @property
    def datacadastro(self):
        return self.__datacadastro
    @property
    def cliente(self):
        return self.__cliente
    @property
    def fornecedor(self):
        return self.__fornecedor
    @property
    def funcionario(self):
        return self.__funcionario
    @property
    def nome(self):
        return self.__nome
    @property
    def ativo(self):
        return self.__ativo

    #Setters
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    @celular.setter
    def celular(self, celular):
        self.__celular = celular
    @email.setter
    def email(self, email):
        self.__email = email
    @datacadastro.setter
    def funcionario(self, datacadastro):
        self.__datacadastro = datacadastro

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
    @fornecedor.setter
    def fornecedor(self, fornecedor):
        self.__fornecedor = fornecedor
    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario
    @ativo.setter
    def funcionario(self, ativo):
        self.__ativo = ativo

class Funcionario(Pessoa):
    #(self, codigo, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo,
    # telefone, celular, email, datacadastro)
    def __init__(self, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj,  ativo, telefone,
                 celular, email, datacadastro, login, senha='', codigo=None):
        super().__init__(codigo, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo, 
                         telefone, celular, email, datacadastro)
        self.__login    =   login
        self.__senha    =   senha

    #Propriedades
    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    # Métodos Getter's e Setters
    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha

class Fornecedor(Pessoa):
    #(self, codigo, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo,
    # telefone, celular, email, datacadastro)
    def __init__(self, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo, telefone,
                 celular, email, datacadastro, razaosocial, codigo=None):
        super().__init__(codigo, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo, telefone, celular,
                         email, datacadastro)
        self.__razaosocial = razaosocial

    #Propriedades
    @property
    def razaosocial(self):
        return self.__razaosocial
    @razaosocial.setter
    def razaosocial(self, razaosocial):
        self.__razaosocial = razaosocial

class Cliente(Pessoa):
    #(self, codigo, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo,
    # telefone, celular, email, datacadastro)
    def __init__(self, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo, telefone,
                 celular, email, datacadastro, codigo=None):
        super().__init__(codigo, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo, telefone, celular,
                         email, datacadastro)



class ContaExtrato:
    def __init__(self, nome, descricao, agencia, numero_conta, saldo_inicial, ativo, codigo = None):
        self.__codigo        = codigo
        self.__nome          = nome
        self.__descricao     = descricao
        self.__agencia       = agencia
        self.__numero_conta  = numero_conta
        self.__saldo_inicial = saldo_inicial
        self.__ativo         = ativo

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_numero_conta(self):
        return self.__numero_conta

    def set_numero_conta(self, numero_conta):
        self.__numero_conta = numero_conta


    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia= agencia

    @property
    def saldo_inicial(self):
        return self.__saldo_inicial

    @saldo_inicial.setter
    def saldo_inicial(self, saldo_inicial):
        self.__saldo_inicial = saldo_inicial

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo


class Lancamento():
    def __init__(self, valor, documento, historico_observacao,
                 cod_cond_pagamento, parcela,data_emissao, data_vencimento, 
                 cod_subcategoria, debito_credito = False, cod_pessoa='',valor_final='',cod_funcionario='',  
                 cod_conta_extrato ='', juros='', desconto='',data_pagamento='',data_efetivacao='', 
                 cod_form_pagamento='', nivel_negociacao='',codigo=None ):
            
        self.__codigo               = codigo
        self.__cod_pessoa           = cod_pessoa
        self.__cod_funcionario      = cod_funcionario
        self.__cod_conta_extrato    = cod_conta_extrato
        self.__valor                = valor
        self.__juros                = juros
        self.__desconto             = desconto
        self.__valor_final          = valor_final
        self.__documento            = documento
        self.__historico_observacao = historico_observacao
        self.__cod_cond_pagamento   = cod_cond_pagamento
        self.__parcela              = parcela
        self.__data_emissao         = data_emissao
        self.__data_vencimento      = data_vencimento
        self.__data_pagamento       = data_pagamento
        self.__data_efetivacao      = data_efetivacao
        self.__cod_form_pagamento   = cod_form_pagamento
        self.__cod_subcategoria     = cod_subcategoria
        self.__nivel_negociacao     = nivel_negociacao
        self.__debito_credito       = debito_credito
        self.__debitocredito        = debitocredito

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def cod_pessoa(self):
        return self.__cod_pessoa

    @cod_pessoa.setter
    def cod_pessoa(self, cod_pessoa):
        self.__cod_pessoa = cod_pessoa

    @property
    def cod_funcionario(self):
        return self.__cod_funcionario
    
    @cod_funcionario.setter
    def cod_funcionario(self, cod_funcionario):
        self.__cod_funcionario = cod_funcionario
    
    @property
    def cod_conta_extrato(self):
       return self.__cod_conta_extrato

    @cod_conta_extrato.setter
    def cod_conta_extrato(self, cod_conta_extrato):
        self.__cod_conta_extrato = cod_conta_extrato
    
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def juros(self):
        return self.__juros

    @juros.setter
    def juros(self, juros):
        self.__juros = juros

    @property
    def desconto(self):
        return self.__desconto

    @desconto.setter
    def desconto(self, desconto):
        self.__desconto = desconto

    @property
    def valor_final(self):
        return self.__valor_final
    
    @valor_final.setter
    def valor_final(self, valor_final):
        self.__valor_final = valor_final

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, documento):
        self.__documento = documento
    
    @property
    def historico_observacao(self):
        return self.__historico_observacao

    @historico_observacao.setter
    def historico_observacao(self, historico_observacao):
        self.__historico_observacao = historico_observacao

    @property
    def cod_cond_pagamento(self):
        return self.__cod_cond_pagamento
    
    @cod_cond_pagamento.setter
    def cod_cond_pagamento(self, cod_cond_pagamento):
        self.__cod_cond_pagamento = cod_cond_pagamento

    @property
    def parcela(self):
        return self.__parcela

    @parcela.setter
    def parcela(self, parcela):
        self.__parcela = parcela
    
    @property
    def data_emissao(self):
        return self.__data_emissao

    @data_emissao.setter
    def data_emissao(self, data_emissao):
        self.__data_emissao = data_emissao
    
    @property
    def data_vencimento(self):
        return self.__data_vencimento
    
    @data_vencimento.setter
    def data_vencimento(self, data_vencimento):
        self.__data_vencimento = data_vencimento

    @property
    def data_pagamento(self):
        return self.__data_pagamento
    
    @data_pagamento.setter
    def data_pagamento(self, data_pagamento):
        self.__data_pagamento = data_pagamento

    @property
    def data_efetivacao(self):
        return self.__data_efetivacao
    
    @data_efetivacao.setter
    def data_efetivacao(self, data_efetivacao):
        self.__data_efetivacao = data_efetivacao
    
    @property
    def cod_form_pagamento(self):
        return self.__cod_form_pagamento

    @cod_form_pagamento.setter
    def cod_form_pagamento(self, cod_form_pagamento):
        self.__cod_form_pagamento = cod_form_pagamento
    
    @property
    def cod_subcategoria(self):
        return self.__cod_subcategoria

    @cod_subcategoria.setter
    def cod_subcategoria(self, cod_subcategoria):
        self.__cod_subcategoria = cod_subcategoria

    @property
    def nivel_negociacao(self):
        return self.__nivel_negociacao
    
    @nivel_negociacao.setter
    def nivel_negociacao(self, nivel_negociacao):
        self.__nivel_negociacao = nivel_negociacao

    @property
    def debito_credito(self):
        return self.__debito_credito
    
    @debito_credito.setter
    def debito_credito(self, debito_credito):
        self.__debito_credito = debito_credito
		
    def debitocredito(self):
        return self.__debitocredito

    @debitocredito.setter
    def debitocredito(self, debitocredito):
        self.__debitocredito = debitocredito
