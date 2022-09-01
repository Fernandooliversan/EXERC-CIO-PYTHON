#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
arquivo = float(input('Informe o tamanho do Arquivo em MB:'))
velocidade = float(input('Velocidade do link da internet:'))
velocidadeMbs = velocidade/8
print(arquivo/velocidadeMbs)/60
