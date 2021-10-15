class Pessoa:
    #Metódo construtor
    def __init__(self, codigo, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj):

        #Atributos Privados
        self.__codigo           = codigo
        self.__nome             = nome
        self.__cliente          = cliente
        self.__fornecedor       = fornecedor
        self.__funcionario      = funcionario
        self.__endereco         = endereco
        self.__cpf              = cpf
        self.__cnpj             = cnpj


        print("Cliente ", self.__nome, " cadastrado(a) com sucesso!")

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

    #Métodos da Entidade
    def imprime_dados_pessoa(self):
        print("-----------DADOS ENTIDADE-----------")
        print("Código     ----- {}".format(self.__codigo))
        print("Nome       ----- {}".format(self.__nome))
        print("Endereço   ----- {}".format( self.__endereco))

        print("\nTipo Entidade:")
        if self.__cliente == True:
            print("Cliente [X]")
        else:
            print("Cliente [ ]")

        if self.__fornecedor == True:
            print("Fornecedor [X]")
        else:
            print("Fornecedor [ ]")

        if self.__funcionario == True:
            print("Funcionário [X]")
        else:
            print("Funcionário [ ]")

        print("\n")

    #Definição de atributos da classe como propriedade
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

    #Setters
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
    @fornecedor.setter
    def fornecedor(self, fornecedor):
        self.__fornecedor = fornecedor
    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario

        
class Funcionario(Pessoa):
    def __init__(self, codigo, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, login, senha):
        super().__init__(codigo, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj)

        self.__login = login
        self.__senha = senha

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