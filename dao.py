import pyodbc
#https://www.sqlshack.com/performing-crud-operations-with-a-python-sql-library-for-sql-server/
from models import Funcionario

SQL_CRIA_PESSOA =           'INSERT INTO PESSOA(NOME, ENDERECO, CPF, CNPJ, CLIENTE, FORNECEDOR, ' \
                            'FUNCIONARIO, LOGIN, SENHA, ATIVO) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
SQL_CRIA_CONTA_EXTRATO  =   'INSERT INTO CONTA_EXTRATO(NOME, DESCRICAO, AGENCIA, NUMERO_CONTA, SALDO_INICIAL, ATIVO)' \
                            'VALUES(?, ?, ?, ?, ?, ?)'
conn = pyodbc.connect('Driver={SQL Server};' +
                      'Server=DESKTOP-M3PBHAT\TESTE_DB;' +
                      'Database=SISTEMA_FINANCEIRO;' +
                      'UID=sa;' +
                      'PWD=2021financesys;' +
                      'Trusted_Connection=no;')
cursor = conn.cursor()
cursor.execute(SQL_CRIA_PESSOA, 'teste', 'teste', 'teste', 'teste', True, True, True, '', '', True)
conn.commit()