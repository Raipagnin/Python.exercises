#crie um programa que leia um valor (dinheiro) e faca uma conversao de real pra dolar, considere 1 real=3,27 dolares
r = float(input('Qtdade de reais:'))
d = r/3.27
print('A cotacao do dia eh 1 real = 3,27 dolares... MITO chora\nseu valor compra {:.2f}U$\nVai querer ou nao, seu pobre miseravel?'.format(d))
#float arredonda pra cima!!!

