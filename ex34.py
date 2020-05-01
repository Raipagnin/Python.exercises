#pegue o salario de um funcionario e de 15% de aumento caso o salario seja ate 1250 e acima disso um aumento de 10%
sal = float(input('Qual eh o seu salario em reais?: '))
if sal <= 1250.00:
    print('Seu salario final eh de: {:.2f} reais'.format(sal + (15 * sal /100)))
else:
    print('Seu salario final eh de: {:.2f} reais'.format(sal + (10 * sal / 100)))

# de acordo com o guanabara eh mais facil se vc criar mais variaveis, pois caso mude o codigo, eh mais facil alterar a variavel
'''if sal <= 1250:
    new = sal + (sal * 15 / 100)
else:
    new = sal + (sal * 10 / 100)
print('seu novo salario eh de: {} reais'.format(new))'''



