sexo = (input("Qual e o seu sexo(M/F)? : "))
idade = int(input("Digite sua idade : "))

if sexo == "M" and idade >= 21:
    print("Voce e maior de idade")

else:
    print ("Voce ainda e menor de idade")

if sexo == "F" and idade >= 18:
    print("Voce e maior de idade") 

else:
    print("Voce ainda e menor de idade")           
        