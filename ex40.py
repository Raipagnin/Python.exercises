#media de aluno, dessa vez falando se passou, recuperacao ou repetiu
from time import sleep
cor = {'cle': '\033[m', 'red': '\033[1;31m', 'gre': '\033[1;32m', 'yel': '\033[4;33m', 'blu': '\033[1;34m'}
x = float(input('Digite a {}primeira{} nota: '.format(cor['blu'], cor['cle'])))
y = float(input('Digite a {}segunda{} nota: '.format(cor['blu'], cor['cle'])))
media = (x + y) / 2
print('Calculando...')
sleep(2)
print('Sua media eh de {}{:.1f}{}'.format(cor['blu'], media, cor['cle']))
if media >= 7:
    print('{}Parabens{}, vc foi {}APROVADO{}!!'.format(cor['gre'], cor['cle'], cor['gre'], cor['cle']))
elif media < 4.9:
    print('Que pena, mas vc foi {}REPROVADO{}'.format(cor['red'], cor['cle']))
else:
    print('OK, vc esta de {}RECUPERACAO{}'.format(cor['yel'], cor['cle']))
# para calcula entre uma nota e outr tb poderia colocar "if 7 > media <=5: