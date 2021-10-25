#https://www.sqlshack.com/performing-crud-operations-with-a-python-sql-library-for-sql-server/
from models import Funcionario, ContaExtrato

SQL_CRIA_CONTA_EXTRATO          =   'INSERT INTO CONTA_EXTRATO(NOME, DESCRICAO, AGENCIA, NUMERO_CONTA, SALDO_INICIAL, ATIVO)' \
                                    'VALUES(?, ?, ?, ?, ?, ?)'

SQL_BUSCA_CONTAS                =   "SELECT COD, NOME, DESCRICAO, AGENCIA, NUMERO_CONTA, SALDO_INICIAL, " \
                                    "IIF(ATIVO = 1, 'Ativo', 'Desativado') as ATIVO FROM CONTA_EXTRATO "

SQL_CRIA_PESSOA                 =   "INSERT INTO PESSOA(NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO, LOGIN, " \
                                    "SENHA, ATIVO, RAZAO_SOCIAL, TELEFONE, CELULAR, EMAIL) " \
                                    "VALUES(?, ?, ?, ?, " \
                                    " ?, ?, ?, ?, '123', ?, ?, ?, ?, ?)"

SLQ_BUSCA_FUNCIONARIOS          =   'SELECT COD, NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO, LOGIN, ' \
                                    'SENHA, ATIVO, RAZAO_SOCIAL, TELEFONE, CELULAR, EMAIL, DATA_CADASTRO ' \
                                    'FROM PESSOA ' \
                                    'ORDER BY COD'

SLQ_BUSCA_FUNCIONARIO_LOGIN     =  'SELECT COD, LOGIN, SENHA ' \
                                    'FROM PESSOA ' \
                                    'WHERE ATIVO = 1 '

class ContaExtratoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, conta_extrato):
        cursor = self.__db.cursor()
        dados_conta_extrato_insercao = [conta_extrato.get_nome(), conta_extrato.get_descricao(), conta_extrato.agencia,
                                        conta_extrato.get_numero_conta(), conta_extrato.saldo_inicial, conta_extrato.ativo]
        if not(conta_extrato.get_codigo()):
            cursor.execute(SQL_CRIA_CONTA_EXTRATO, dados_conta_extrato_insercao)
        self.__db.commit()
        return conta_extrato

    def listar(self):
            cursor = self.__db.cursor()
            cursor.execute(SQL_BUSCA_CONTAS)
            contas = traduz_contas(cursor.fetchall())
            return contas



class FuncionarioDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, funcionario):
        cursor = self.__db.cursor()
        #"INSERT INTO PESSOA(NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO, LOGIN, " \
        #"SENHA, ATIVO, RAZAO_SOCIAL, TELEFONE, CELULAR, EMAIL) " \
        dados_funcionario_Insercao = [  funcionario.get_nome(), funcionario.get_endereco(), funcionario.get_cpf(),
                                funcionario.get_cnpj(), funcionario.cliente, funcionario.fornecedor,
                                funcionario.funcionario, funcionario.login, funcionario.ativo,
                                funcionario.razaosocial, funcionario.telefone, funcionario.celular, funcionario.email]

        if not(funcionario.get_codigo()):
            cursor.execute(SQL_CRIA_PESSOA, dados_funcionario_Insercao)
        self.__db.commit()
        return funcionario

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SLQ_BUSCA_FUNCIONARIOS)
        funcionarios = traduz_funcionarios(cursor.fetchall())
        return funcionarios

    def busca_por_id(self, cod):
        cursor = self.__db.cursor()
        cursor.execute(SLQ_BUSCA_FUNCIONARIO_LOGIN)
        tupla = cursor.fetchone()

        # (self, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, login, ativo, telefone,
        #         celular, email, datacadastro, razaosocial, codigo=None, senha='')
        return Funcionario(codigo=tupla[0], login=tupla[1], senha=tupla[2], nome='', cliente='',
                           fornecedor=False, funcionario=True, endereco='', cpf='', cnpj='',
                           ativo=True, telefone='', celular='', email='', datacadastro='', razaosocial='')



def traduz_funcionarios(funcionarios):
    def cria_funcionario_com_tupla(tupla):
        #         0    1       2       3    4      5           6           7         8
        #'SELECT COD, NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO, LOGIN, ' \
        #   9      10        11         12        13      14          15
        #'SENHA, ATIVO, RAZAO_SOCIAL, TELEFONE, CELULAR, EMAIL, DATA_CADASTRO ' \

        #(self, nome, cliente, fornecedor, funcionario, endereco, cpf, cnpj, login, ativo, telefone,
        #         celular, email, datacadastro, razaosocial, codigo=None, senha='')
        return Funcionario(nome=tupla[1], cliente=tupla[5], fornecedor=tupla[6], funcionario=tupla[7],
                           endereco=tupla[2], cpf=tupla[3], cnpj=tupla[4], login=tupla[8], ativo=tupla[10],
                           telefone=tupla[12], celular=tupla[13], email=tupla[14], datacadastro=tupla[15],
                           razaosocial=tupla[11], codigo=tupla[0])

    return list(map(cria_funcionario_com_tupla, funcionarios))

def traduz_contas(contas):
    def cria_conta_com_tupla(tupla):
        return ContaExtrato(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], codigo=tupla[0])
    return list(map(cria_conta_com_tupla, contas))



