#mostre todos os numeros pares de 1-50
print('Numeros pares de 1 - 50')
for c in range(2, 51, 2):
    print(c, end=' ') # vc poderia usar uma formula matematica em que vc pega o modulo % por 2 == 0, nesse caso
    # o processador faria mais movimentos ao inves de fazer como no exemplo a cima... pense que as vezes nao eh questao de mais ou menos linhas e sim menos trabalho
