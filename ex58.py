#jogo de advinhar o numero do pc, porem, tentar de novo ate acertar aquele numero pensado
from random import randint
from time import sleep
pc = randint(0, 10)  # faz o computador sortear
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente advinhar!')
print('-=-' * 20)
pl = int(input('Em que numero estou pensando?: '))
num = 1
print('PROCESSANDO...')
sleep(1)
while pl != pc:
    if pl < pc:
        pl = int(input('Tente um numero MAIOR: '))
    else:
        pl = int(input('Tente um numero MENOR: '))
    num += 1
print('Parabens, foi o numero {} e vc tentou acertar em {}x'.format(pc, num))

############################# agora a do guanabara
from random import randint
pc = randint(0, 10)  # faz o computador sortear
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente advinhar!')
print('-=-' * 20)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual eh o seu palpite? '))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais, tente novamente')
        else:
            print('Menos, tente novamente')

print('Parabens, vc acertou em {} palpites'.format(palpite))
