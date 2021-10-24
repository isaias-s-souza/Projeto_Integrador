#https://www.sqlshack.com/performing-crud-operations-with-a-python-sql-library-for-sql-server/
from models import Funcionario, ContaExtrato

SQL_CRIA_PESSOA =           'INSERT INTO PESSOA(NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO, LOGIN, ' \
                            'SENHA, ATIVO) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
SQL_CRIA_CONTA_EXTRATO  =   'INSERT INTO CONTA_EXTRATO(NOME, DESCRICAO, AGENCIA, NUMERO_CONTA, SALDO_INICIAL, ATIVO)' \
                            'VALUES(?, ?, ?, ?, ?, ?)'
SLQ_BUSCA_FUNCIONARIOS  =   'SELECT COD, NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO, LOGIN, ' \
                            'SENHA, ATIVO FROM PESSOA'
SQL_BUSCA_CONTAS        =   "SELECT COD, NOME, DESCRICAO, AGENCIA, NUMERO_CONTA, SALDO_INICIAL, " \
                            "IIF(ATIVO = 1, 'Ativo', 'Desativado') as ATIVO FROM CONTA_EXTRATO"


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

        dados_funcionario_Insercao = [  funcionario.get_nome(), funcionario.get_endereco(), funcionario.get_cpf(),
                                        funcionario.get_cnpj(), funcionario.cliente, funcionario.fornecedor,
                                        funcionario.funcionario, funcionario.login, funcionario.get_senha(),
                                        funcionario.ativo]

        if not(funcionario.get_codigo()):
            cursor.execute(SQL_CRIA_PESSOA, dados_funcionario_Insercao)
        self.__db.commit()
        return funcionario

#    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SLQ_BUSCA_FUNCIONARIOS)
        funcionarios = traduz_funcionarios(cursor.fetchall())
        return  funcionarios

def traduz_funcionarios(funcionarios):
    def cria_funcionario_com_tupla(tupla):
        return Funcionario(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6],
                           tupla[7], tupla[8], tupla[9], tupla[10], codigo= tupla[0])
    return list(map(cria_funcionario_com_tupla,funcionarios))

def traduz_contas(contas):
    def cria_conta_com_tupla(tupla):
    # nome, descricao, agencia, numero_conta, saldo_inicial, ativo, codigo = None
        return ContaExtrato(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], codigo=tupla[0])
    return list(map(cria_conta_com_tupla,contas))



