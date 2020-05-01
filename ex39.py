#calcule idade atraves de ano de nascimento e calcule se deve ou nao se alistar ou se ja passou do tempo
from datetime import date
today = date.today().year
dob = int(input('Qual o ano de nascimento?: '))
age = today - dob
print('Quem nasceu no ano de {} tem {} anos no ano atual de {}'.format(dob, age, today))
if age < 18:
    print('Vc ainda nao tem 18 anos e deve se alistar no ano de {}'.format(today + (18 - age)))
elif age > 18:
    print('Vc ja passou dos 18 anos e deveria ter se alistado em {}'.format(today - (age - 18)))
else:
    print('Vc tem 18 anos e deve se alistar nesse ano de {}'.format(today))
# ao inves de colocar dentro do format vc pode criar variaveis pra essa diferenca de idade, porem menos linhas assim,
#mas tb vc tendo variaveis, se vc precisar dessa info depois vc pode acessar facilmente