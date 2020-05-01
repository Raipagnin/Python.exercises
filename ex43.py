# calcule imc
from time import sleep
peso = float(input('Qual seu peso em Kg: '))
altura = float(input('Qual sua altura em m: '))
imc = peso / (altura ** 2)
print('Calculando seu IMC')
sleep(0)
print('Seu IMC eh {:.2f}'.format(imc))
if 0 < imc < 18.5:
    print('Vc esta ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Vc esta no PESO NORMAL')
elif 25 <= imc < 30:
    print('Vc esta acima do peso')
elif 30 <= imc < 40:
    print('Vc esta OBESO')
elif 40 <= imc < 100:
    print('Vc esta OBESO MORBIDO')
else:
    print('O valor inserido eh INVALIDO')




