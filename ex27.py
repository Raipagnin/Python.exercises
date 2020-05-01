#Analise um nome e de seu primeiro e ultimo nome
name = str(input('Digite seu nome completo: ')).strip().title()
print('Ola, mto prazer em te conhecer, {}!'.format(name))
list = name.split()
print('Seu primeiro nome eh {}'.format(list[0]))
print('Seu ultimo nome eh {}'.format(list[-1]))

