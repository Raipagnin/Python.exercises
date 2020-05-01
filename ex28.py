# peca ao usario para advinhar um numero entre 1 e 5 e o computador deve escolher um e ver se esta correto
from random import randint
from time import sleep
pc = randint(0, 5)  # faz o computador sortear
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar!')
print('-=-' * 20)
pl = int(input('Em que numero estou pensado?: '))
print('PROCESSANDO...')
sleep(2)  # esse metodo poe o computador para 'dormir' por tantos segundos
if pl == pc:
    print('Parabens, pensamos no mesmo numero: {}'.format(pc))
else:
    print('Que pena! Nao foi dessa vez. Eu pensei no num {}'.format(pc))
