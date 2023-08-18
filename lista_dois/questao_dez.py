salario_bruto = float(input("Digite o seu salario bruto : "))

imposto_um = (salario_bruto * 0.075) - 142.80
valor_um = 7.5 
deducao_um = 142.80 
imposto_dois = (salario_bruto * 0.15) - 548.82
valor_dois = 15
deducao_dois = 548.82
imposto_tres = (salario_bruto * 0.225) - 636.13
valor_tres = 22.5
deducao_tres = 636.13
imposto_quatro = (salario_bruto * 0.227) - 869.36
valor_quatro = 22.7
deducao_quatro = 869.36


if salario_bruto < 1903.98:
    print ("Voce e isento de impostos a pagar")

elif salario_bruto > 1903.99 and salario_bruto <= 2826.65:
    print(f"Voce tera que pagar {valor_um} de impostos e {deducao_um} de deducao, ao todo voce tera que pagar o valor de {round (imposto_um,2)}")

elif salario_bruto > 2826.66 and salario_bruto <= 3751.05:
    print(f"Voce tera que pagar {valor_dois} de impostos e {deducao_dois} de deducao, ao todo voce tera que pagar o valor de {round (imposto_dois,2)}")

elif salario_bruto > 3751.06 and salario_bruto <= 4664.68:
    print(f"Voce tera que pagar {valor_tres} de impostos e {deducao_tres} de deducao, ao todo voce tera que pagar o valor de {round (imposto_tres,2)}")

elif salario_bruto > 4664.68:
    print(f"Voce tera que pagar {valor_quatro} de impostos e {deducao_quatro} de deducao, ao todo voce tera que pagar o valor de {round (imposto_quatro,2)}")
