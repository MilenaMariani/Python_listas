nome = (input("Digite seu nome : "))
nota_um = float (input("Digite sua nota : "))
nota_dois = float (input("Digite sua segunda nota : "))
media_das_notas = (nota_um + nota_dois) / 2 

if media_das_notas < 5:
    print(f"Voce esta reprovado , sua nota foi {media_das_notas}.")

elif media_das_notas >= 5 and  media_das_notas < 7:
    print(f"Voce esta de recuperacao, sua nota foi {media_das_notas}")

elif media_das_notas >=7 and media_das_notas <= 10:
    print("Voce esta aprovado!")