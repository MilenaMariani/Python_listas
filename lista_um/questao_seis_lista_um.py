volume = float (input("Qual o valume da esfera : "))
area = float (input("Digite o valor da area : "))
raio = float (input("Qual o valor do raio : "))

volume = (4/3) * 3.14 * (pow (raio,3))
area = (4 * 3.14) * (pow(raio,2))

print (f"O valume sra {volume} e a superficie e {area}")