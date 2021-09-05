from Entidade import Entidade

def print_hi(name):
    print(f'Hi,{name}')
if __name__ == '__main__':


    cliente1 = Entidade(1,"Maria Aparecida da Silva",True,False,False,"AV: Afonso Pena,233, Centro, Muzambinho-MG")
    cliente1.imprime_dados_entidade()

    fornecedor1 = Entidade(2, "Alfalagos LTDA", False, True, False, "Rua: Lindolfo Coimbra, 63, Galpão 2, Jd.Margaridas, Alfenas-MG")
    fornecedor1.imprime_dados_entidade()

    fornecedor1 = Entidade(3, "Juliana Passos de Almeida", False, False, True, "Rua : Cristóvão Colombo, 621, Centro, Caconde-SP")
    fornecedor1.imprime_dados_entidade()