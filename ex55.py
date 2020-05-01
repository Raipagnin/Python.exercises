#leia 5 pesos de 5 pessoas e diga qual eh o mais pesado e qual eh o menos pesado
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da {} pessoa?: '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso eh de {} e o menor eh {}'.format(maior, menor))

# existe uma funcao pra facilitar que eh de pesos... .append que te max e min
