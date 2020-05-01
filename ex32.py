#calcule se o ano dado eh bissexto. sao anos divisiveis por 4. excetos multiplos de 100 que nao sao divisiveis por 400 ex: 1700, 1900
from datetime import date
year = int(input('Que ano vc quer analisar?Coloque 0 para analisar o seu ano atual: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} eh BISSEXTO'.format(year))
else:
    print('O ano {} nao eh BISSEXTO'.format(year))
