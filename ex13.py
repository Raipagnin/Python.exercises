# com o salario mensal de um empregado mostre o valor mais 15% de aumento

s = float(input('Qual eh o seu salario mermao?: '))
a = s + (15*s/100)


print('Seu salario eh de {:.2f}reais, com seu aumento de 15\nSeu salario final eh de {:.2f}reais'.format(s, a))
