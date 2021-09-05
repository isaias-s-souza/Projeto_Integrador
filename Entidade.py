class Entidade:
    def __init__(self, codigo, nome, ehCliente, ehFornecedor, ehFuncionario, endereco):

        #Atributos Privados
        self.__codigo           = codigo
        self.__nome             = nome
        self.__ehCliente        = ehCliente
        self.__ehFornecedor     = ehFornecedor
        self.__ehFuncionario    = ehFuncionario
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
        return self.__ehCliente

    def set_cliente(self, eh_cliente):
        self.__ehCliente = eh_cliente

    # É FORNECEDOR
    def get_fornecedor(self):
        return self.__ehFornecedor

    def set_fornecedor(self, eh_fornecedor):
        self.__ehFornecedor = eh_fornecedor

    # É FUNCIONÁRIO
    def get_funcionario(self):
        return self.__ehFuncionario

    def set_funcionario(self, eh_funcionario):
        self.__ehFuncionario = eh_funcionario

    #ENDEREÇO
    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    #Métdos da Entidade
    def imprime_dados_entidade(self):
        print("\n-----------DADOS ENTIDADE-----------")
        print("Codigo     ----- {}".format(self.__codigo))
        print("Nome       ----- {}".format(self.__nome))
        print("Endereco   ----- {}".format( self.__endereco))
        if self.__ehCliente == True:
            print("Tipo Entidade   ----- Cliente")
        if self.__ehFornecedor == True:
            print("Tipo Entidade   ----- Fornecedor")
        if self.__ehFuncionario == True:
            print("Tipo Entidade   ----- Funcionário")