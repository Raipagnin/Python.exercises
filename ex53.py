#analise se uma frase eh um palindromo (ler de tras pra frente o mesmo de frente pra tras)
x = str(input('Digite uma frase: ')).strip().upper()
words = x.split() #dessa maneira tiro os espacos entre palavras
sentence = ''.join(words)
inverse = ''
for l in range(len(sentence) - 1, -1, -1): # uma maneira mais simples eh {::-1] para ler de tras pra frente
    inverse += sentence[l]
print('O inverso da sua frase {} eh {}'.format(sentence, inverse))
if sentence == inverse:
    print('EH uma palindromo')
else:
    print('NAO eh um palindromo')
#uma mais simples, porem, no caso nao se usa o for *o objetivo era usar o for*

frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")