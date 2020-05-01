# opcoes de 1-5, sendo soma, multiplicacao, maior/menor, novos num, e sair. fazer loop e qdo escolher opcao errada, falar errado e tente novamente
print('{:=^50}\n{: ^50}\n{:=^50}'.format('', 'Digite dois valores e escolha entre as opcoes', ''))
x = float(input('Digite primeiro valor: '))
y = float(input('Digite segundo valor: '))
z = 0
while z != 5:
    print('''   
    [1] somar
    [2] multiplicar
    [3] maior/menor
    [4] novos valores
    [5] sair do programa''') # dentro de aspas triplas nao se usa identacao, no caso aqui perceba que no run aparece espacada
    z = int(input('>>> Qual eh a sua opcao?: '))
    if z == 1:
        print('A soma de {} e {} eh igual {}'.format(x, y, x + y)) # nao esqueca que vc pode fazer variaveis pra soma... caso va usar depois essa info
    elif z == 2:
        print('O valor {} x {} eh igual a {}'.format(x, y, x * y))
    elif z == 3:
        if x < y:
            print('O valor {} eh maior que {}'.format(y, x))
        elif x > y:
            print('O valor {} eh maior {}'.format(x, y))
        elif x == y:
            print('Os dois valores sao iguais')
    elif z == 4:
        x = float(input('Digite novo valor:'))
        y = float(input('Digite novo valor: '))
    elif z == 5:
        print('FIM, volte sempre!')
    else:
        print('OPCAO INVALIDA\nTente Novamente')
    print('-=-' * 20)
# com a resposta do guanabara eu achei falho pois nao tinha opcao para caso os numeros fossem iguais
