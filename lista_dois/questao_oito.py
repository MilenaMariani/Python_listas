distancia = float(input ("Qual foi a distancia que o carro pecorreu em Km? : "))
gasolina= float(input("Quantos foi o consumo de gasolina por litro? : "))
consumo = (distancia / gasolina)

if consumo < 8:
    print("Venda o carro!")

elif consumo <= 8 and consumo <= 14:
    print("Economico")

elif consumo > 12:
    print("super economico!")