numero1 = int (input("Digite o primeiro numero desejado : "))
numero2 = int (input("Digite o segundo numero desejado : "))
numero3 = int (input("Digite o terceiro numero desejado : "))

if numero1 > numero2 and numero1 > numero3:
    print(f"o numero {numero1} e maior que o {numero2} e {numero3}")

elif numero2 > numero1 and numero2 > numero3:
    print (f"O numero {numero2} e maior que o  numero {numero1} e maior que o numero {numero3}")

elif numero3 > numero1 and numero3 > numero2:
    print (f"o numero {numero3} e o maior que o numero {numero1} e maior que numero {numero2}")