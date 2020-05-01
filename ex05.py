# ex 5 - faca um programa que leia um numero inteiro, e mostre na tela o numero, o antecessor e o sucessor
x = int(input('Digite um valor:'))
a = x - 1
s = x + 1
print('Baseado no valor {}, seu antecessor eh {} e seu sucessor eh {}'.format(x, a, s))
# vc tb pode fazer tudo com apenas uma variavel e dentro do .format colocar a equacao, porem se colocam variaveis a mais, caso use depois em outras linhas