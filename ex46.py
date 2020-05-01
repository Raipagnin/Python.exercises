#laco for... contagem regressiva para estourar fogos de artificio
from time import sleep
cor = {'cle': '\033[m', 'red': '\033[1;31m', 'gre': '\033[1;32m', 'yel': '\033[1;33m', 'blu': '\033[1;34m'}
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('{}POW{} POW {}PRRRIIIII {}FSSFXSSSS {}BOOOM{}'.format(cor['red'], cor['yel'], cor['blu'], cor['gre'], cor['red'],
                                                             cor['cle']))
#o ultimo termo eh sempre ignorado, por isso teve de ser colocado -1 ao inves de 0
