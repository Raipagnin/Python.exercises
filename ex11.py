#construa um programa que ao colocar largura e altura de uma superficie (parede) vc calcula a area e assim calcula area em m2 e qtos litros de tinta
# eh preciso pra pintar uma parede, sendo que 1 litro de tinta pinta 2m2

a = float(input('Digite Altura: '))
l = float(input('Digite Largura: '))
a2 = a*l
t = a2/2
print('Considerando sua area {:.2f}, vc precisara usar {:.2f} litros de tinta'.format(a2, t))
