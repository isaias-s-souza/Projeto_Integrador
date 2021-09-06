from Entidade import Entidade

EnderecoEntidade = "AV: Afonso Pena,233, Centro, Muzambinho-MG"
entidade1 = Entidade(1, "Maria Aparecida da Silva", True, False, False, EnderecoEntidade)
entidade1.imprime_dados_entidade()

EnderecoEntidade = "Rua: Lindolfo Coimbra, 63, Galpão 2, Jd.Margaridas, Alfenas-MG"
entidade2 = Entidade(2, "Alfalagos LTDA", False, True, False, EnderecoEntidade)
entidade2.imprime_dados_entidade()

EnderecoEntidade = "Rua : Cristóvão Colombo, 621, Centro, Caconde-SP"
entidade3 = Entidade(3, "Juliana Passos de Almeida", False, False, True, EnderecoEntidade)
entidade3.imprime_dados_entidade()

