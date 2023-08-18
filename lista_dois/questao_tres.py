idade_pessoa1 = int (input("Digite a idade da primeira pessoa : "))
idade_pessoa2 = int (input("Digite a idade da segunda pessoa : "))

nome_pessoa1 = (input("Digite seu nome : "))
nome_pessoa2 = (input("Digite seu nome : "))
ano_pessoa1 = (input("Digite a sua data de nascimento"))
ano_pessoa2 =  (input("Digite a sua data de nascimento"))


ano_atual = int (input("Digite o ano atual"))
ano_pessoa1 = (ano_pessoa1) [6:9]
ano_pessoa2 =  (ano_pessoa1) [6:9]

calculo_1 = ano_atual - ano_pessoa1
calculo_2 = ano_atual - ano_pessoa2


if calculo_1 > calculo_2:
    print(f"{nome_pessoa1} e mais velha que {nome_pessoa2}")

else:
    print(f"{nome_pessoa2} e mais velha que {nome_pessoa1}")        