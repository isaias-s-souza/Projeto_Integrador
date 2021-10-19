#https://www.sqlshack.com/performing-crud-operations-with-a-python-sql-library-for-sql-server/

SQL_CRIA_PESSOA =           'INSERT INTO PESSOA(NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, FUNCIONARIO, LOGIN, ' \
                            'SENHA, ATIVO) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
SQL_CRIA_CONTA_EXTRATO  =   'INSERT INTO CONTA_EXTRATO(NOME, DESCRICAO, AGENCIA, NUMERO_CONTA, SALDO_INICIAL, ATIVO)' \
                            'VALUES(?, ?, ?, ?, ?, ?)'



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