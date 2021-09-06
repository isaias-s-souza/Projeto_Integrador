class Entidade:
    def __init__(self, codigo, nome, cliente, fornecedor, funcionario, endereco):

        #Atributos Privados
        self.__codigo           = codigo
        self.__nome             = nome
        self.__cliente          = cliente
        self.__fornecedor       = fornecedor
        self.__funcionario      = funcionario
        self.__endereco         = endereco


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
    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, eh_cliente):
        self.__cliente = eh_cliente

    # É FORNECEDOR
    def get_fornecedor(self):
        return self.__fornecedor

    def set_fornecedor(self, eh_fornecedor):
        self.__fornecedor = eh_fornecedor

    # É FUNCIONÁRIO
    def get_funcionario(self):
        return self.__funcionario

    def set_funcionario(self, eh_funcionario):
        self.__funcionario = eh_funcionario

    #ENDEREÇO
    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    #Métodos da Entidade
    def imprime_dados_entidade(self):
        print("\n-----------DADOS ENTIDADE-----------")
        print("Codigo     ----- {}".format(self.__codigo))
        print("Nome       ----- {}".format(self.__nome))
        print("Endereco   ----- {}".format( self.__endereco))

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

    # Setters
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
