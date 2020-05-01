#calculo de fatorial. ex: fatorial de 6 = 6x5x4x3x2x1 =720
from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} eh igual a {}'.format(n, f))
# maneira mais simples... logicamente nao pode usar assim
n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1 #pq eh multiplicacao vc tem que comecar com 1 ao invez de zero, pq numero x 0 eh sempre zero, enquanto que num x 1 eh sempre o mesmo num
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x 'if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))
#agora usando for
n = int(input('Digite um numero para calcular seu fatorial: '))
c = 0
f = 1
for c in range(1, n):
    f *= n
    n -= 1
print('Seu fatorial é {}.'.format(f))
#outro com for
fat = int(input('Digite um número: '))
for c in range(fat - 1, 0, -1):
    fat = fat * c
print('O fatorial desse número é: {}.'.format(fat))