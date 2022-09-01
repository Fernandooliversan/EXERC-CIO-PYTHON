#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo
n1 = int(input(" Digite o numero inteiro"))
n2 = int(input(" Digite novamente o numero inteiro"))
n3 = float(input("Digite um número real"))
produto = (n1*2)*(n2/2)
soma = (n1*3)+n3
elevado = n3 **3
print("O produto do dobro do primeiro com metade do segundo:" , produto)
print ("A soma do triplo do primeiro com terceiro" , soma)
print ("o terceiro elevado ao cubo" , elevado)