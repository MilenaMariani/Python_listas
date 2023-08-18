valor_Maca = 1.30
valor_BananaKG = 5.00

compra_Maca = float (input("Digite quantas macas foi comprada : "))
compra_bananaKG = float (input("Digite quantos KG de banana foi comprada : ")) 
#cada quilo da banana e igual a 5 reias, ou seja, se tiver 4 kg , vai ser 4*5


calculo_Maca = (valor_Maca * compra_Maca)
calculo_Banana = (valor_BananaKG * compra_bananaKG)

print (f"A compra das macas ao final em reias foi : R$ {calculo_Maca}")
print (f"A compra das banana ao final em reias foi : R$ {calculo_Banana}")
print (f"O total das compras foi : {calculo_Banana + calculo_Maca}")


