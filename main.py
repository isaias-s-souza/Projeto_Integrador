from Entidade import Entidade

print("\n")
EnderecoEntidade = "AV: Afonso Pena,233, Centro, Muzambinho-MG"
entidade1 = Entidade(1, "Maria Aparecida da Silva", True, False, False, EnderecoEntidade)
entidade1.imprime_dados_entidade()

print("Motivo atualização dados (NOME): Maria sabendo sobre seus direitos de acordo com a LGPD, "
      "solicitou conferir seu nome no cadastro,\npois descobriu que seu nome constava errado "
      "na sua antiga identidade\n")
print(entidade1.nome)
entidade1.set_nome("Maria Aparecida Silva")
print("Seu nome foi corrigido no cadastro! (", entidade1.get_nome(), ")\n")

print("\n")
EnderecoEntidade = "Rua: Lindolfo Coimbra, 63, Galpão 2, Jd.Margaridas, Alfenas-MG"
entidade2 = Entidade(2, "Alfalagos LTDA", False, True, False, EnderecoEntidade)
entidade2.imprime_dados_entidade()

print("\n")
EnderecoEntidade = "Rua : Cristóvão Colombo, 621, Centro, Caconde-SP"
entidade3 = Entidade(3, "Juliana Passos de Almeida", False, False, True, EnderecoEntidade)
entidade3.imprime_dados_entidade()
print("Motivo atualização dados (TIPO ENTIDADE): Juliana veio na loja, fora do seu horário de trabalho comprar,\n"
      "e atualizou seu cadastro também como cliente...\n")
entidade3.cliente = True
entidade3.imprime_dados_entidade()



