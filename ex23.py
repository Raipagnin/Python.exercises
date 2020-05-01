#analise um numero dando unidade, dezena, centena e milhar
num = int(input('Type an integer number: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unity: {}\nDecimal: {}\nCentennial: {}\nMilennial: {}'.format(u, d, c, m))
#jeito mais dificil do caralho de fazer, vou deixar aberto pq em outra aula ele ensina algo mais facil que nao requer matematica
