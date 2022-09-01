#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area = float(input("Digite o tamanho da área: "))
litro = area/3
print ("Quantidade de Litros:", area*litro)
print ("Quantidade de Latas:", (area*litro)/18)
print ("Custo Total:R$", ((area*litro)/18) * 80)