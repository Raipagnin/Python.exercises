#pegar um numero e dar 3 escolhas, binario, octal, hexagonal e resolver
num = int(input('Digite um numero inteiro: '))
print('[1] - para BINARIO\n[2] - para OCTAL\n[3] - para HEXADECIMAL')
x = int(input('Escolha uma das opcoes: '))
if x == 1:
    print('{} em valor BINARIO eh {}'.format(num, bin(num)[2:]))
elif x == 2:
    print('{} em OCTAL eh igual a {}'.format(num, oct(num)[2:]))
elif x == 3:
    print('{} em Hexa eh igual a {}'.format(num, hex(num)[2:]))
else:
    print('Esse opcao nao eh valida para nossa conversao')


