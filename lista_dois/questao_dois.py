elocidade_carro1 = float (input ("Digite a velocidade do carro1 : "))
velocidade_carro2 = float (input ("Digite a velocidade do carro2 : "))

distancia_pecorrida_carro1 = float (input("Digite a distancia pecorrida do carro1 : "))
distancia_pecorrida_carro2 = float (input("Digite a distancia pecorrida do carro2 : "))

tempo_pecorrido_carro1 = float(input("Qual foi o tempo pecorrido carro1 : "))
tempo_pecorrido_carro2 = float(input("Qual foi o tempo pecorrido carro2 : "))

velocidade_media1 = distancia_pecorrida_carro1/tempo_pecorrido_carro1
velocidade_media2 = distancia_pecorrida_carro2/tempo_pecorrido_carro2

if velocidade_media1 >= velocidade_media2:
    print (f"O carro1 teve uma velocidade maior que o carro2, ou seja, o carro um teve {round(velocidade_media1,2)} de velocidade, com o tempo de {tempo_pecorrido_carro1 }, e uma distancia de {distancia_pecorrida_carro1}")

else:
    print(f"O carro2 teve uma velociade maior que o carro1,ou seja, o carro um teve {round(velocidade_media2,2)} de velocidade, com o tempo de {tempo_pecorrido_carro2 }, e uma distancia de {distancia_pecorrida_carro2}")