altura_parede= int (input("qual e a altura da parede? : "))
largura_parede = int (input("qual e a largura da parede? :"))
altura_azulejo = int (input ("qual e a altura do azulejo? :"))
largura_azulejo= int (input ("qual e a largura do azulejo"))

area_parede= altura_parede * largura_parede
print (area_parede)

area_azulejo= altura_azulejo * largura_azulejo
print(area_azulejo)

azulejos_necessarios= area_azulejo / area_parede

print ("serao necessarios" + str(azulejos_necessarios))