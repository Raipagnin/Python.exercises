#pergune nome, idade e sexo de 4 pessoas, analise a media de idade, qual o nome e idade do homem mais velho e qtas mulheres com menos de 20 anos
somaid = 0
maiorid = 0
nomevelho = ''
totf = 0
for p in range(1, 5):
    print('------ {} PESSOA ------'.format(p))
    nome = str(input('NOME: ')).strip()
    id = int(input('IDADE: '))
    sexo = str(input('SEXO [F/M]: ')).strip()
    somaid += id
    if p == 1 and sexo in 'Mm': #pode transformar a string em upper ou lower tb
        maiorid = id
        nomevelho = nome
    if sexo in 'Mm' and id > maiorid:
        maiorid = id
        nomevelho = nome
    if sexo in 'Ff' and id < 20:
        totf += 1
print('A media de idade dessas pessoas eh de {} anos'.format(somaid / 4)) # pode fazer a variavel por fora caso va usar essa info depois
print('O homem mais velho tem {} anos e se chama {}'.format(maiorid, nomevelho))
print('Um total de {} mulheres com menos de 20 anos'.format(totf))
# ainda existem cenaerios nao tratados, como responder como invalido caso digitem um sexo diferente de f ou m, ou no
#caso de haver so mulheres e nenhum homem e ainda exisir o print para homem mais velho e idade