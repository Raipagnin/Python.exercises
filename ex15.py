# escreve um programa que pergunte a qtdade de dias e km rodados de um carro alugado e de o valor a ser pago. 60/dia e 0,15/km
x = int(input('Insira o valor de dias em que o carro foi alugado: '))
y = float(input('Insira qtos Km foram rodados nesses dias de aluguel: '))
z = (x * 60) + (y * 0.15)
print('De acordo com a qtdade de dias de aluguel do carro {:.0f}\nE {:.3f}Km rodados nesse periodo\nO valor total a ser pago eh de {:.2f}R$'.format(x, y, z)
