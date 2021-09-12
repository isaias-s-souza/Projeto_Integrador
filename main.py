from Pessoa import Pessoa

print("\n")
EnderecoPessoa = "AV: Afonso Pena,233, Centro, Muzambinho-MG"
pessoa1 = Pessoa(1, "Maria Aparecida da Silva", True, False, False, EnderecoPessoa)
pessoa1.imprime_dad
os_pessoa()

print("Motivo atualização dados (NOME): Maria sabendo sobre seus direitos de acordo com a LGPD, "
      "solicitou conferir seu nome no cadastro,\npois descobriu que seu nome constava errado "
      "na sua antiga identidade\n")
print(pessoa1.nome)
pessoa1.set_nome("Maria Aparecida Silva")
print("Seu nome foi corrigido no cadastro! (", pessoa1.get_nome(), ")\n")

print("\n")
EnderecoPessoa = "Rua: Lindolfo Coimbra, 63, Galpão 2, Jd.Margaridas, Alfenas-MG"
pessoa2 = Pessoa(2, "Alfalagos LTDA", False, True, False, EnderecoPessoa)
pessoa2.imprime_dados_pessoa()

print("\n")
EnderecoPessoa = "Rua : Cristóvão Colombo, 621, Centro, Caconde-SP"
pessoa3 = Pessoa(3, "Juliana Passos de Almeida", False, False, True, EnderecoPessoa)
pessoa3.imprime_dados_pessoa()
print("Motivo atualização dados (TIPO ENTIDADE): Juliana veio na loja, fora do seu horário de trabalho comprar,\n"
      "e atualizou seu cadastro também como cliente...\n")
pessoa3.cliente = True
pessoa3.imprime_dados_pessoa()



