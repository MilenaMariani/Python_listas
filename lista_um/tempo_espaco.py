posicao_Inicial = 2
velocidade = 3 
aceleracao = 10
espaco_Pecorrido = 0
tempo_Pecorrido = float (input("Digite o tempo pecorrido : "))

espaco_Pecorrido = (espaco_Pecorrido + posicao_Inicial * tempo_Pecorrido + 1/2 * aceleracao) * pow (tempo_Pecorrido,2)

print (f"O espaco pecorrido nesse tempo e : {espaco_Pecorrido}")

