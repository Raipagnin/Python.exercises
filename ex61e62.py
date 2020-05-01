#PA com while
print('{}\n{:^}\n{}'.format('-='*20, 'PROGRESSAO ARITMETICA', '-='*20))
num = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a razao: '))
termo = num
cont = 1
total = 0
mais = 10 #pq inicialmente se mostra 10 termos da pa
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ..> '.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Qtos termos mais vc quer mostrar? '))
print('Progressao finalizada com {} termos'.format(total))
#outra resolucao
p_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 10
while c > 0:
    print(p_termo, end=' ')
    p_termo += razao
    c -= 1
    if c == 0:
        c = int(input('\nAcrescentar mais números na sequência: '))
# porem essa solucao nao conta qtos termos foram feitos que era parte do exercicio tb... pq se vc comeca com um contador
#sendo 10 e na primeira sequencia vc os 10 termos ate zerar, e depois reinicia um contador que vai ate 0... como contar os termos?





