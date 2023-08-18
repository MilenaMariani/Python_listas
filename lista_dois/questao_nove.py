sexo = (input("Qual e o sexo(F/M) : "))
peso = float (input("Qual e o seu peso? : "))
altura = float (input("Qual e a sua altura em cm? : "))
idade = int (input("Qual e a sua idade : "))

homem = 66 + (13.7 * peso) + (5.0 * altura) - (6.8 * idade)
mulher = 665 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)

if sexo == "F":
    print(f"O valor ideal de calorias para voce e : {round(mulher,2)}")

elif sexo == "M":
    print(f"o valor ideal de calorias para voce e : {round(homem,2)}")