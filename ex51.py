#resolva uma progressao aritmetica
print('{}\n{}\n{}'.format('-='*20, 'PROGRESSAO ARITMETICA', '-='*20))
a = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a razao: '))
termo = a + (10 - 1) * r  #para calcular o decimo termo (e nao os 10 primeiros numeros de uma pa, precisa fazer o
for c in range(a, termo + r, r):                        #primeiro termo + o termo que vc quer expressar (no caso decimo
    print('{} '.format(c), end='..> ')                  # menos 1 e * pela razao... ai mostra os 10 resultados de um pa
print('Acabou')                     #foi necessario colocar no contador termo + 1 (ou r) para mostrar a ultima posicao que
                                    # o python nao mostra. ex como colocar 11 pra mostrar ate o 10

# agora um jeito mais simples:
num = int(input('Digite o Primeiro número da PA: '))
razão = int(input('Digite a Razão da PA: '))
for c in range(1, 11):
    print(num, end=' ..> ')
    num += razão
print('Acabou')

#mais simples ainda:

p = int(input('Primeira: '))
r = int(input('Razão: '))
for X in range(0, 10):
    print(r * X + p, end=' ..> ')
