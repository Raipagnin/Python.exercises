#nome completo, ponha em caps e minus, analise qtdade de letras sem espacos, mais primeiro nome e letras
name = str(input('What\'s your full name: ')).strip()
name1 = name.split()
print('Your full name in lower is: {}'.format(name.lower()))
print('Your name in CAPS is: {}'.format(name.upper()))
print('The amount of letters on your name are: {}'.format(len(name) - name.count(' ')))
#print('Your first name is {}, and the amount of letters in it are {}'.format(name1[0], len(name1[0])))
print('Seu primeiro nome tem {} letras'.format(name.find(' ')))
