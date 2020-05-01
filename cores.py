# colocando cores, codigo basico eh \033[m, entre o colchetes e m, vc tem 3 opcoes para colocar
cor = {'limpa': '\033[m',
       'blu': '\033[34m',
       'gre': '\033[32m',
       'yel': '\033[33m',
       'red': '\033[31m'}
# eh melhor qdo vc monta esse dicionario qdo vc vai usar as mesmas cores varias vezes
x = str(input('Digite o seu nome: '))
y = int(input('Digite a sua idade: '))
if y >= 20:
    print('Mto prazer, {}{}{}! Nao queria te dizer mas vc eh mto {}velho{}!'.format(cor['blu'], x, cor['limpa'],
                                                                                    cor['red'], cor['limpa']))
