#mesmo que ex 65, porem usando flag
cont = soma = 0
while True:
    num = int(input('Digite um valor [999] - para parar: '))
    if num == 999:
        break
    cont += 1
    soma += num
print('A soma dos valores eh {} e foram {} valores'.format(soma, cont))
print('FIM')
