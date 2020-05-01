# faca um programa que calcule a soma de todos os numeros impares e multiplos de 3 que estejam entre 1 -500
soma = 0
cont = 0
for s in range(1, 501, 2):
    if s % 3 == 0:
        cont += 1
        soma += s
print('A soma de todos esses numeros eh {}, sendo que foram {} numeros no total'.format(soma, cont))

