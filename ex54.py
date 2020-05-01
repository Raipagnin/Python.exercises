#pergunte 7 pessoas seu ano de nascimento e diga qtos sao maiores de idade e qtos sao menores
from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for c in range(1, 8):
    ano = int(input('Qual o ano de nascimento da {} pessoa: '.format(c)))
    idade = atual - ano
    if idade >= 21:
        tmaior += 1

    else:
        tmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade e {} pessoas menores de idade'.format(tmaior, tmenor))

#outra maneira mais simples porem confusa

from datetime import date
menores = 0
for c in range(1, 8):
    pessoa = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if date.today().year - pessoa < 21:
        menores += 1
print('\n{} são Maiores e {}são menores.'.format(7 - menores, menores))


