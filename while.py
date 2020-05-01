#o while se usa qdo nao se sabe direito os limites... se vc nao sabe um range ou nao existe um padrao, use o while
#ex com o for:
'''for c in range(1, 10):
    print(c, end=' ')
print('FIM')'''
#no while fica:
c = 1
while c < 10:
    print(c, end=' ')
    c += 1  # ou 'c = c +1', pq vc quer pegar e somar todos os passos. pega o 1, faz o loop e volta pro 1 de novo e
    # agora vc vai somar ao segundo
# agora digamos que vc precisa colocar um valor, porem nao sabe qtos valores serao?:
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM') # o programa vai rodar ate que vc digite 0, pois nao ha mais valores a serem adicionados
# vc tb pode colocar uma flag como r = [S/N] e colocar a condicao while r == S, depois do valor, pergunte com um input
# se quer continuar a colocar valores... ex:
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM')
# na proxima aula ele ensina um jeito melhor pra interromper while
