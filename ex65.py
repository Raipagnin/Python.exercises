s = 'S'
cont = media = soma = maior = menor = 0
while s in 'Ss':
    n = int(input('Digite um numero: '))
    cont += 1
    soma += n
    if n == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor: # existe uma diferenca se vc fizer elif ao inves de if
            menor = n
    s = str(input('Digite para continuar [S/N]: ')).upper().strip()[0] #de novo o zero entre colchetes so lera a primeira letra
media = soma / n
print('Vc usou {} valores e a media eh {:.2f}\nSendo o maior {} e o menor eh {}'.format(cont, media, maior, menor))
print('FIM')
# existem mtos erros ainda a corrigir com o [s/n], se coloca numero sai do programa, se coloca vazio e enter da erro
