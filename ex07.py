# desenvolva um programa que leia duas notas de um aluno e calcule sua media

n = str(input('Digite seu nome: '))
print('Ola {}, seu(a) viado(a), seja bem vindo!\nFavor digitar abaixo suas notas horriveis para calcular sua media:'.format(n))
n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
m = (n1+n2)/2
print('A media de suas notas bostas eh {:.2f}'.format(m))



