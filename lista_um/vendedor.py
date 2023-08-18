carros_Vendidos = int (input("Quantos carros foram vendidos? : "))
total_Vendas = float (input("Qual foi o valor total de suas vendas? : "))
salario_Fixo = float(input("Qual e o seu salario fixo? : "))
comissao_PorVendas = float (input("Qual e a comissao recebida por cada venda? : "))

total_Vendas = (total_Vendas * 0.05)

salario_final= (salario_Fixo + comissao_PorVendas * carros_Vendidos + 5 * total_Vendas/100)

print (f"O valor do seu salario final e de : {salario_final} ")