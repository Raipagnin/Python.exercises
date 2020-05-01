#crie um game jokenpo
import emoji
from random import choice
from time import sleep
cor = {'cle': '\033[m', 'red': '\033[1;31m', 'gre': '\033[1;32m', 'yel': '\033[4;33m', 'blu': '\033[1;34m'}
print('{:=^40}\nSUAS OPCOES:\n[1] - {}\n[2] - {}\n[3] - {}'.format('JOGO JOKENPO',
                                                                   emoji.emojize(':punch:', use_aliases=True),
                                                                   emoji.emojize(':hand:', use_aliases=True),
                                                                   emoji.emojize(':v:', use_aliases=True)))
escolha = int(input('what\'s your play?: '))
pedra = emoji.emojize(':punch:', use_aliases=True)
papel = emoji.emojize(':hand:', use_aliases=True)
tesoura = emoji.emojize(':v:', use_aliases=True)
print('{}JO{}'.format(cor['red'], cor['cle']))
sleep(1)
print('{}KEN{}'.format(cor['blu'], cor['cle']))
sleep(1)
print('{}PO{}'.format(cor['gre'], cor['cle']))
sleep(1)
pc = choice([pedra, papel, tesoura])
if escolha == 1:
    print('Vc jogou {} e o computador jogou {}'.format(pedra, pc))
    if pc == pedra:
        print('FOI UM {}EMPATE!{}'.format(cor['yel'], cor['cle']))
    elif pc == tesoura:
            print('{}PARABENS, vc VENCEU!{}'.format(cor['gre'], cor['cle']))
    else:
        print('O Computador {}VENCEU!{}'.format(cor['red'], cor['cle']))
elif escolha == 2:
    print('Vc jogou {} e o computador jogou {}'.format(papel, pc))
    if pc == papel:
        print('FOI UM {}EMPATE!{}'.format(cor['yel'], cor['cle']))
    elif pc == pedra:
        print('{}PARABENS, vc VENCEU!{}'.format(cor['gre'], cor['cle']))
    else:
        print('O Computador {}VENCEU!{}'.format(cor['red'], cor['cle']))
elif escolha == 3:
    print('Vc jogou {} e o computador jogou {}'.format(tesoura, pc))
    if pc == tesoura:
        print('FOI UM {}EMPATE!{}'.format(cor['yel'], cor['cle']))
    elif pc == papel:
        print('{}PARABENS, vc VENCEU!{}'.format(cor['gre'], cor['cle']))
    else:
        print('O Computador {}VENCEU!{}'.format(cor['red'], cor['cle']))
else:
    print('ESCOLA INVALIDA.\nTente Novamente!')



