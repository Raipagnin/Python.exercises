# crie um algoritimo em que leia um numero, mostre seu dobro, seu triplo e raiz quadrada

x = int(input('Digite um valor:'))
d = x*2
t = x*3
rq = x**(1/2)

print('Baseado no seu valor {}, seu dobro eh {}, seu triplo eh {}, e sua raiz quadrada eh {:.2f}'.format(x, d, t, rq))

#menos linhas, melhor.... tente usar tudo dentro do .format caso nao se va usar esses valores apos isso

