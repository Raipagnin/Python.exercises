#leia 6 num inteiros e mostre a soma de somente os pares
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Vc informou {} numero(s) par(es) e a soma desse(s) par(es) foi {}'.format(cont, soma))

