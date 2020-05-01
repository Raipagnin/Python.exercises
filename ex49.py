# tabuada refeita com laco for do ex 09
n = int(input('Digite um numero pra sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))

    #comparacao com ex09
    '''n = int(input('Digite um valor: '))
print('Levando em consideracao que todo numero multiplicado por zero sempre sera zero:\n{} x  1 = {}\n{} x  2 = {}\n{}'
      ' x 3 = {}\n{} x  4 = {}\n{} x  5 = {}\n{} x  6 = {}\n{} x  7 = {}\n{} x  8 = {}\n{} x  9 = {}\n{} x 10 = '
      '{}'.format(n, n*1, n, n*2, n, n*3, n, n*4, n, n*5, n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))'''