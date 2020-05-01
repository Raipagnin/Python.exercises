#coloque 3 medidas e analise se pode formar um triangulo. existencia de triangulo se baseia em um dos segmentos tem de ser menor que os outros 2
print('-=-' * 20)
print('ANALISADOR DE TRIANGULO')
print('-=-' * 20)
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Parabens, vc consegue formar um triangulo')
else:
    print('Que pena! Infelizmente vc nao consegue formar um triangulo')


