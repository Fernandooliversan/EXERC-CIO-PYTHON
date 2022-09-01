#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9)
Fahrenheit  = float(input("Digite a Temperatura em Fahrenheit:"))
trans = 5* ((Fahrenheit-32) / 9)
print("Temperatura em Graus Celsius:" , trans , "graus")