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
'''style for font:0, 1, 4, 7
0 - none, regular
1 - bold
4 - underline
7 - negative'''
''' background colour follows regular colour by difference of decimal number 40 instead of 30
ex: font colour 30 = white, background colour 40 = white
30/40 = white    31/41 = red      32/42 = green      33/43 = yellow       34/44 = blue
35/45 = magenta(purple)     36/46 = cian         37/47 = grey
