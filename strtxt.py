# textos e strings
frase = '''The job market for cybersecurity is growing rapidly, according to Cybersecurity Ventures. Get started in securing the future with
our free online cybersecurity prep course, developed in partnership with one of the top-ranked cybersecurity bootcamps on SwitchUp.'''
print(frase[2::4]) #primeiro numero sera da onde comecar a analise do texto, segundo numero sendo o final e terceiro sendo de qtos em qtos espacos pular e mostrar
#se vc nao quer colocar comeco ou fim, vc pode colocar um : vazio 
print(len(frase)) #len para contar qqtas letras tem.... se colocar frase.strip retira os espacos extras antes e depois da frase comecar/terminar
print(frase.count('o'))
print(frase.upper().count('O')) #vc pode combinar coisas, ao colocar upper eu transformei a frase toda em maiscula, assim logo apos eu pude contar qtos 'O' tinha
print(frase.replace('cybersecurity', 'meucu')) # veja que so foi trocada cybersec com c minusculo
print('online' in frase)
print(frase.find('online'))
print(frase.find('ONline'))
dividido = frase.split()
print(dividido)
print(dividido[1]) # ao dividir eu formei uma lista, qdo eu peco 1, eu estou pedindo o item numero 1 da lista, nao esqueca que comeca do 0... enquanto que
#numa string o 0 seria a primeira letra de tudo, e 1 sendo a segunda letra, em um split onde se da uma lista, vc pega o item da lista
print(dividido[2][4]) # assim vc pega o item 2 da lista (terceira palavra sendo market) e pede para que seja mostrado a posicao 3 dessa palavra
print(frase.upper())
print(frase.lower())











