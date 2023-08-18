quant_hastes = int (input("Qual foi a quantidade de hastes compradas? : "))
qual_hastes = (input("Qual foi o tipo de haste comprado (aco/aluminio/cobre) : "))

haste_aco = 2.50
haste_cobre = 4.00
haste_aluminio = 5.0

desconto_acima_de_7 = 0.10
desconto_acima_de_15 = 0.15
desconto_acima_de_20 = 0.20

calculo_hastes_acima_de_7_aco = (quant_hastes * haste_aco) - desconto_acima_de_7
calculo_hastes_acima_de_15_aco = (quant_hastes * haste_aco) - desconto_acima_de_15
calculo_hastes_acima_de_20_aco = (quant_hastes * haste_aco) - desconto_acima_de_20


calculo_hastes_acima_de_7_cobre = (quant_hastes * haste_cobre) - desconto_acima_de_7
calculo_hastes_acima_de_15_cobre = (quant_hastes * haste_cobre) - desconto_acima_de_15
calculo_hastes_acima_de_20_cobre = (quant_hastes * haste_cobre) - desconto_acima_de_20


calculo_hastes_acima_de_7_aluminio = (quant_hastes * haste_aluminio) - desconto_acima_de_7
calculo_hastes_acima_de_15_aluminio = (quant_hastes * haste_aluminio) - desconto_acima_de_15
calculo_hastes_acima_de_20_aluminio = (quant_hastes * haste_aluminio) - desconto_acima_de_20

if quant_hastes <= 6:
    print(f"O total d hastes compradas foi {quant_hastes}, por isso nao tera desconto")

elif quant_hastes >= 7 and quant_hastes <= 15 and qual_hastes == "aco":
    print (f"A quantidade de hastes compradas foi de {quant_hastes}, entao com o desconto o valor total e : {calculo_hastes_acima_de_7_aco}")    

elif quant_hastes >= 16 and quant_hastes <= 20 and qual_hastes == "aco":
    print (f"A quantidade de hastes compradas foi de {quant_hastes}, entao com o desconto o valor total e : {calculo_hastes_acima_de_15_aco}")

elif quant_hastes > 20 and qual_hastes == "aco":    
    print (f"A quantidade de hastes compradas foi de {quant_hastes}, entao com o desconto o valor total e : {calculo_hastes_acima_de_20_aco}")


elif quant_hastes >= 7 and quant_hastes <= 15 and qual_hastes == "cobre":
    print (f"A quantidade de hastes compradas foi de {quant_hastes}, entao com o desconto o valor total e : {calculo_hastes_acima_de_7_cobre}")    

elif quant_hastes >= 16 and quant_hastes <= 20 and qual_hastes == "cobre":    
    print (f"A quantidade de hastes compradas foi de {quant_hastes}, entao com o desconto o valor total e : {calculo_hastes_acima_de_15_cobre}")

elif quant_hastes > 20 and qual_hastes == "cobre": 
    print (f"A quantidade de hastes compradas foi de {quant_hastes}, entao com o desconto o valor total e : {calculo_hastes_acima_de_20_cobre}")


elif quant_hastes >= 7 and quant_hastes <= 15 and qual_hastes == "aluminio":
    print (f"A quantidade de hastes compradas foi de {quant_hastes}, entao com o desconto o valor total e : {calculo_hastes_acima_de_7_aluminio}")    

elif quant_hastes >= 16 and quant_hastes <= 20 and qual_hastes == "aluminio":    
    print (f"A quantidade de hastes compradas foi de {quant_hastes}, entao com o desconto o valor total e : {calculo_hastes_acima_de_15_aluminio}")

elif quant_hastes > 20 and qual_hastes == "aluminio": 
     print (f"A quantidade de hastes compradas foi de {quant_hastes}, entao com o desconto o valor total e : {calculo_hastes_acima_de_20_aluminio}")

