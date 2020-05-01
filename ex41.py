#classificacao de atletas por data de nascimento
from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
hj = date.today().year
idade = hj - ano
print('O atleta tem {} anos'.format(idade))
if 3 <= idade <= 9:
    print('Classificacao: MIRIM')
elif 10 <= idade <= 14:
    print('Classificacao: INFANTIL')
elif 15 <= idade <= 19:
    print('Classificacao: JUNIOR')
elif 20 <= idade <= 25:
    print('Classificacao: SENIOR')
elif 100 > idade > 25:
    print('Classificacao: MASTER')
else:
    print('O seguinte(s) erro(s) foram detectados:\n- A faixa etaria do atleta nao se encaixa na idade minima para '
          'competir.\n- O valor eh invalido!\nTente Novamente!')


