#pergunte a velocidade do carro. se for acima de 80km/h multe a pessoa valendo 7,00 o km extra
vel = float(input('Qtos km/h vc estava dirigindo?: '))
if vel > 80:
    print('Vc ultrapassou o limite! Sua multa eh de {:.2f} reais'.format((vel - 80) * 7))
print('Continue abaixo do Limite e Tenha um BOM DIA, seu corno')

#nem sempre precisara colocar else