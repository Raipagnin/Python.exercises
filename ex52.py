# leia um numero e veja se ele eh primo ou nao
n = int(input('Digite um numero inteiro: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes '.format(c, t))
if t == 2:
    print('E por isso o numero EH PRIMO!')
else:
    print('E por isso o numero NAO eh PRIMO!')
print('\033[33mFIM\033[m')

#outra forma mais simples??

num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

print("O número {} foi divisível {} vezes!".format(num, contador))

if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")

