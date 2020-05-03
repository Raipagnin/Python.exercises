#com a aula 15 vc consegue resolver um problema daqui melhor
print('{:-^50}'.format(' Tratando de valores '))
num = cont= soma = 0
while num != 999:
    num = int(input('Digite um numero [999] para parar: '))
    soma += num
    cont += 1
print('Vc digitou {} numeros e a soma entre eles eh {}'.format(cont-1, soma-999))
print('FIM')
