media = float (input("Qual e a sua media de notas? : "))
faltas = int  (input("Digite o numero de faltas : "))

if media >= 7 and faltas <=32:
    print("Voce esta aprovado! ")

elif media < 7 and faltas  <=32:
    print("Voce esta reprovado. ")

elif media >= 7 and faltas > 32:
    print("Voce esta reprovado por faltas.")

elif media < 7 and faltas > 32:
    print("Voce esta reprovado por faltas e por media. ")