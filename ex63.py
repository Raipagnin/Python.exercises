#sequencia de fibonacci, primeiros 10 termos: 0.1.1.2.3.5.8.13.21... que eh a soma do termos anteriores
print('{}\n{}\n{}'.format('-='*20, ' SEQUENCIA FIBONACCI ', '-='*20))
ntermo = int(input('Qtos termos quer calcular?: '))
n1, n2 = 0, 1
cont = 0
if ntermo <= 0:
    print('Coloque um numero valido e inteiro')
#elif ntermo == 1:
   #print('Sequencia Fibonacci de {} eh : {}'.format(ntermo, n1))# nem eh necessario para o funcionamento
else:
    print('Sequencia Fibonacci:')
    while cont < ntermo:
        print(n1, end=' ..> ')
        nt = n1 + n2
        n1 = n2
        n2 = nt
        cont += 1
print('FIM')
# agora do guanabara
n = int(input('Qtos termos quer mostrar: '))
t1, t2 = 0, 1
print('{} ..> {}'.format(t1, t2), end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('..> {}'.format(t3), end=' ') # uma vez que vc ja tenha printado o t3, vc anda uma casa e muda
    t1 = t2
    t2 = t3
    cont += 1
print('..> FIM')


