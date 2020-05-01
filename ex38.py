#leia dois num int e compare dizendo qual eh maior, menor ou igual ao outro
x = float(input('Digite o primeiro numero: '))
y = float(input('Digite o segundo numero: '))
if x > y:
    print('O PRIMEIRO eh maior que o SEGUNDO')
elif x < y:
    print('O SEGUNDO eh maior que o PRIMEIRO')
else:
    print('Ambos os numeros sao IGUAIS')
