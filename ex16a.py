#mostre a parte inteira de um numero real
from math import trunc
x = float(input('digite um valor real: '))
print('a porcao inteira do valor {} eh {}'.format(x, trunc(x)))
#se vc so importa math sem usar from, vc tem que colocar o codigo math.trunc(x) para pedir o truncate, se vc so pede o codigo em si
#como nesse caso, vc pode colocar direto trunc
'''uma maneira interessante tb eh simplesmente colocar int(num), por ex dentro do .format(x, int(x)) assim so mostrando o mesmo numero do input so que inteiro'''