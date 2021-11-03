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

    def set_cpf(self, cnpj):
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
        self.__codigo   =   codigo
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
        self.__codigo=codigo
        self.__razaosocial = razaosocial

    #Propriedades
    @property
    def razaosocial(self):
        return self.__razaosocial
    @razaosocial.setter
    def razaosocial(self, razaosocial):
        self.__razaosocial = razaosocial



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