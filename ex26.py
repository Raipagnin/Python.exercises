# analise uma frase e sua letra a. total, primeira e ultima
a = str(input('Digite uma frase: ')).strip().upper()
print('O total de letras A eh {}'.format(a.count('A')))
print('A primeira letra A esta na posicao {}'.format(a.find('A')+1))
print('A ultima letra A esta na posicao {}'.format(a.rfind('A')+1))
