from models import Cliente, Funcionario, ContaExtrato, Fornecedor
class ContaExtratoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, conta_extrato):
        cursor = self.__db.cursor()

        if not(conta_extrato.get_codigo()):
            dados_conta_extrato_insercao = [conta_extrato.get_nome(), conta_extrato.get_descricao(),
                                            conta_extrato.agencia,
                                            conta_extrato.get_numero_conta(), conta_extrato.saldo_inicial,
                                            conta_extrato.ativo]
            SQL_CRIA_CONTA_EXTRATO = 'INSERT INTO CONTA_EXTRATO(NOME, DESCRICAO, AGENCIA, NUMERO_CONTA, SALDO_INICIAL, ATIVO)' \
                                     'VALUES(?, ?, ?, ?, ?, ?)'
            cursor.execute(SQL_CRIA_CONTA_EXTRATO, dados_conta_extrato_insercao)
        self.__db.commit()
        return conta_extrato

    def listar(self):
            cursor = self.__db.cursor()
            SQL_BUSCA_CONTAS = "SELECT COD, NOME, DESCRICAO, AGENCIA, NUMERO_CONTA, SALDO_INICIAL, " \
                               "IIF(ATIVO = 1, 'Ativo', 'Desativado') as ATIVO FROM CONTA_EXTRATO "
            cursor.execute(SQL_BUSCA_CONTAS)
            contas = traduz_contas(cursor.fetchall())
            return contas

def traduz_contas(contas):
    def cria_conta_com_tupla(tupla):
        return ContaExtrato(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], codigo=tupla[0])
    return list(map(cria_conta_com_tupla, contas))

class FuncionarioDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, funcionario):
        cursor = self.__db.cursor()

        if (funcionario.get_codigo()):
            dados_funcionario_atualizacao = [funcionario.get_nome(), funcionario.get_endereco(), funcionario.telefone,
                                             funcionario.celular, funcionario.email, funcionario.get_cpf(),
                                             funcionario.login, funcionario.ativo, funcionario.get_codigo()]

            SQL_ATUALIZA_FUNCIONARIO       = "UPDATE PESSOA SET NOME = ?, ENDERECO = ?,  TELEFONE = ?, CELULAR = ?," \
                                             "EMAIL = ?, CPF = ?, LOGIN = ?, ATIVO = ? " \
                                             "WHERE COD = ?"

            cursor.execute(SQL_ATUALIZA_FUNCIONARIO, dados_funcionario_atualizacao)
        else:

            dados_funcionario_Insercao = [funcionario.get_nome(), funcionario.get_endereco(), funcionario.telefone,
                                         funcionario.celular, funcionario.email, funcionario.get_cpf(),
                                         funcionario.login, funcionario.funcionario, funcionario.ativo]
            SQL_CRIA_PESSOA_FUNCIONARIO = "INSERT INTO PESSOA(NOME, ENDERECO, TELEFONE, CELULAR, EMAIL, CPF," \
                                          "LOGIN, FUNCIONARIO, ATIVO)" \
                                          "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(SQL_CRIA_PESSOA_FUNCIONARIO, dados_funcionario_Insercao)

        self.__db.commit()
        return funcionario

    def listar(self):
        cursor = self.__db.cursor()
        SQL_BUSCA_FUNCIONARIO = 'SELECT COD, NOME, ENDERECO, CPF, LOGIN, ATIVO,' \
                                'TELEFONE, CELULAR, EMAIL, DATA_CADASTRO ' \
                                'FROM PESSOA ' \
                                'WHERE FUNCIONARIO = 1 ORDER BY COD'
        cursor.execute(SQL_BUSCA_FUNCIONARIO)
        funcionarios = traduz_funcionarios(cursor.fetchall())
        return funcionarios

    def busca_por_id(self, login):
        cursor = self.__db.cursor()
        SQL_BUSCA_FUNCIONARIO_LOGIN = 'SELECT COD, LOGIN, SENHA ' \
                                      'FROM PESSOA ' \
                                      'WHERE ATIVO = 1 and LOGIN = ?'
        cursor.execute(SQL_BUSCA_FUNCIONARIO_LOGIN, login)
        tupla = cursor.fetchone()

        # (self, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, login, ativo, telefone,
        #         celular, email, datacadastro, razaosocial, codigo=None, senha='')
        return Funcionario(codigo=tupla[0], login=tupla[1], senha=tupla[2], nome='', cliente=False,
                           fornecedor=False, funcionario=True, endereco='', cpf='', cnpj='',
                           ativo=True, telefone='', celular='', email='', datacadastro='')

def traduz_funcionarios(funcionarios):
    def cria_funcionario_com_tupla(tupla):
        #  0     1       2      3     4      5      
        # COD, NOME, ENDERECO, CPF, LOGIN, ATIVO,' \
        #    6        7        8          9      
        # TELEFONE, CELULAR, EMAIL, DATA_CADASTRO
        
        #(self, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, login, ativo, telefone,
        #         celular, email, datacadastro, codigo=None, senha='')
        dataCadastroFormatada = tupla[9].strftime('%d/%m/%Y')
        
        return Funcionario(nome=tupla[1], endereco=tupla[2], cpf=tupla[3], login=tupla[4], ativo=tupla[5], 
                           telefone=tupla[6], celular=tupla[7], email=tupla[8], datacadastro=dataCadastroFormatada,
                           codigo=tupla[0], cliente=False, fornecedor=False, funcionario=True, cnpj='',
                           senha='')
    
    return list(map(cria_funcionario_com_tupla, funcionarios))

class FornecedorDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, fornecedor):
        cursor = self.__db.cursor()
        SQL_CRIA_PESSOA_FORNECEDOR  =   "INSERT INTO PESSOA(NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO, " \
                                        "ATIVO, RAZAO_SOCIAL, TELEFONE, CELULAR, EMAIL) " \
                                        "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        dados_fornecedor_Insercao = [fornecedor.get_nome(), fornecedor.get_endereco(), fornecedor.get_cpf(),
                                fornecedor.get_cnpj(), fornecedor.cliente, fornecedor.fornecedor,
                                fornecedor.funcionario, fornecedor.ativo, fornecedor.razaosocial,
                                fornecedor.telefone, fornecedor.celular, fornecedor.email]

        if not(fornecedor.get_codigo()):
            cursor.execute(SQL_CRIA_PESSOA_FORNECEDOR, dados_fornecedor_Insercao)
        self.__db.commit()
        return fornecedor

    def listar(self):
        SQL_BUSCA_FORNECEDOR = 'SELECT COD, NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO, ' \
                               'ATIVO, RAZAO_SOCIAL, TELEFONE, CELULAR, EMAIL, DATA_CADASTRO ' \
                               'FROM PESSOA ' \
                               'WHERE FORNECEDOR = 1 ' \
                               'ORDER BY COD'
        cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_FORNECEDOR)
        fornecedor = traduz_fornecedor(cursor.fetchall())
        return fornecedor


def traduz_fornecedor(fornecedor):
    def cria_fornecedor_com_tupla(tupla):
        # 0    1        2       3   4       5       6           7
        #COD, NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO, ' \
        #  8        9           10          11      12      13
        #ATIVO, RAZAO_SOCIAL, TELEFONE, CELULAR, EMAIL, DATA_CADASTRO

        # self, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo, telefone,
        # celular, email, datacadastro, razaosocial, codigo=None
        return Fornecedor(nome=tupla[1], cliente=tupla[5], fornecedor=tupla[6], funcionario=tupla[7],
                           endereco=tupla[2], cpf=tupla[3], cnpj=tupla[4], ativo=tupla[8],
                           telefone=tupla[10], celular=tupla[11], email=tupla[12], datacadastro=tupla[13],
                           razaosocial=tupla[9], codigo=tupla[0])

    return list(map(cria_fornecedor_com_tupla, fornecedor))


class ClienteDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, cliente):
        cursor = self.__db.cursor()
        SQL_CRIA_PESSOA_CLIENTE  =   "INSERT INTO PESSOA(NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO, " \
                                        "ATIVO, TELEFONE, CELULAR, EMAIL) " \
                                        "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        dados_cliente_Insercao = [   cliente.get_nome(), cliente.get_endereco(), cliente.get_cpf(),
                                     cliente.get_cnpj(), cliente.cliente, cliente.fornecedor,
                                     cliente.funcionario, cliente.ativo, cliente.telefone, 
                                     cliente.celular, cliente.email]

        if not(cliente.get_codigo()):
            cursor.execute(SQL_CRIA_PESSOA_CLIENTE, dados_cliente_Insercao)
        self.__db.commit()
        return cliente

    def listar(self):
        SQL_BUSCA_CLIENTE =    'SELECT COD, NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO, ' \
                               'ATIVO, TELEFONE, CELULAR, EMAIL, DATA_CADASTRO ' \
                               'FROM PESSOA ' \
                               'WHERE CLIENTE = 1 ' \
                               'ORDER BY COD'
        cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_CLIENTE)
        cliente = traduz_cliente(cursor.fetchall())
        return cliente


def traduz_cliente(cliente):
    def cria_cliente_com_tupla(tupla):
        # 0    1       2       3    4       5          6            7
        #COD, NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO,
        #  8       9        10       11         12
        #ATIVO, TELEFONE, CELULAR, EMAIL, DATA_CADASTRO

        # self, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, ativo, telefone,
        # celular, email, datacadastro, razaosocial, codigo=None
        return Cliente(nome=tupla[1], cliente=tupla[5], fornecedor=tupla[6], funcionario=tupla[7],
                           endereco=tupla[2], cpf=tupla[3], cnpj=tupla[4], ativo=tupla[8],
                           telefone=tupla[9], celular=tupla[10], email=tupla[11], datacadastro=tupla[12],
                           codigo=tupla[0])

    return list(map(cria_cliente_com_tupla, cliente))



