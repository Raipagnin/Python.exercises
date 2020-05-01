#fazer um jokenpo (de novo) mas pelo guanabara# porem essa porra nao ficou completa qdo vc escolhe opcao invalida...
from random import randint
from time import sleep
cor = {'cle': '\033[m', 'red': '\033[1;31m', 'gre': '\033[1;32m', 'yel': '\033[4;33m', 'blu': '\033[1;34m'}
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas OPCOES:
[0] - Pedra
[1] Papel
[2] Tesoura''')
vc = int(input('Qual eh a sua jogada?: '))
if vc != 0 and vc != 1 and vc != 2:
    print('JOGADA INVALIDA!')
print('{}JO{}'.format(cor['red'], cor['cle']))
sleep(1)
print('{}KEN{}'.format(cor['blu'], cor['cle']))
sleep(1)
print('{}PO{}'.format(cor['gre'], cor['cle']))
sleep(1)
print('-=' * 20)
print('O Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[vc]))
print('-=' * 20)
if pc == 0:
    if vc == 0:
        print('EMPATE')
    elif vc == 1:
        print('Jogador VENCE')
    elif vc == 2:
        print('Computador VENCE')
elif pc == 1:
    if vc == 0:
        print('Computador VENCE')
    elif vc == 1:
        print('EMPATE')
    elif vc == 2:
        print('Jogador VENCE')
elif pc == 2:
    if vc == 0:
        print('Jogador VENCE')
    elif vc == 1:
        print('Computador VENCE')
    elif vc == 2:
        print('EMPATE')
else:
    print('JOGADA INVALIDA')

