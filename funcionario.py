class Funcionario:
    def __init__(self, codigo, nome, cliente, fornecedor, funcionario, endereco, login, senha):
        super().__init__(codigo, nome, cliente, fornecedor, funcionario, endereco)

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

