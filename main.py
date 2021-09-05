from Entidade import Entidade

def print_hi(name):
    print(f'Hi,{name}')
if __name__ == '__main__':

    print("\n-----------DADOS CLIENTE-----------")
    cliente1 = Entidade(1,"Maria Aparecida da Silva",1,0,0,"AV: Afonso Pena,233, Centro, Muzambinho-MG")
    cliente1.imprime_dados_entidade()


    print("\n-----------DADOS FORNECEDOR-----------")
    fornecedor1 = Entidade(2, "Alfalagos LTDA", 0, 1, 0, "Rua: Lindolfo Coimbra, 63, Galpão 2, Jd.Margaridas, Alfenas-MG")
    fornecedor1.imprime_dados_entidade()

    print("\n-----------DADOS FUNCIONÁRIO-----------")
    fornecedor1 = Entidade(3, "Juliana Passos de Almeida", 0, 0, 1, "Rua : Cristóvão Colombo, 621, Centro, Caconde-SP")
    fornecedor1.imprime_dados_entidade()