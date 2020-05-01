#forma de pagamento de uma compra, 1 - vista (10% desc), 2- vista no cartao(5% desc), 3 - 2x no cartao, 3 - +3x no cartao (20% juros)
cor = {'cle': '\033[m', 'red': '\033[1;31m', 'gre': '\033[1;32m', 'yel': '\033[4;33m', 'blu': '\033[1;34m'}
print('{}{:=^40}{}'.format(cor['gre'], ' LOJAS VANESSAO ', cor['cle']))
preco = float(input('Preco das compras: R$ '))
print('{}FORMAS DE PAGAMENTO:{}\n[1] - A vista no dinheiro\n[2] - A vista no cartao\n[3] - 2x no cartao\n[4] - 3x ou '
      'mais no cartao '.format(cor['blu'], cor['cle']))
opcao = int(input('Qual a {}OPCAO{} de pagamento?: '.format(cor['red'], cor['cle'])))
if opcao == 1:
    print('Sua compra de {}R$ {:.2f}{} vai custar {}R$ {:.2f}{} com {}10% de desconto{}'.format(cor['blu'], preco,
                                                                                              cor['cle'], cor['gre'],
                                                                                              preco - (preco * 10 / 100)
                                                                                              , cor['cle'], cor['yel'],
                                                                                              cor['cle']))
elif opcao == 2:
    print('Sua compra de {}R$ {:.2f}{} vai custar {}R$ {:.2f}{} com {}5% de descconto{}'.format(cor['blu'], preco,
                                                                                              cor['cle'], cor['gre'],
                                                                                              preco - (preco * 5 / 100),
                                                                                              cor['cle'], cor['yel'],
                                                                                              cor['cle']))
# na aula ele colocou if para opcao 1 e 2 e ao inves de colocar um print para cada opcao, ele fez duas variaveis de total
#e fez apenas um print generalizado para ambas as opcoes. lembrando que o print estava fora de indexacao, assim o print
#ia acontecer sempre, o que ia mudar era o calculo da variavel de desconto para as duas primeiras opcoes
elif opcao == 3:
    print('Sua compra de {}R$ {:.2f}{} sera dividida em {}2 parcelas{} de {}R$ {:.2f}{}'.format(cor['blu'], preco,
                                                                                              cor['cle'], cor['gre'],
                                                                                              cor['cle'], cor['red'],
                                                                                              preco / 2, cor['cle']))
elif opcao == 4:
    parcela = int(input('Qtas parcelas?: '))
    final = (preco + (preco * 20 / 100)) / parcela
    print('Sua compra de {}R$ {:.2f}{} em {}{}x{} sera no valor mensal de {}R$ {:.2f}{} com {}juros de 20%{} '
          'totalizando {}R$ {:.2f}{}'.format(cor['blu'], preco, cor['cle'], cor['gre'], parcela, cor['cle'], cor['red'],
                                             final, cor['cle'], cor['yel'], cor['cle'], cor['red'],
                                             preco + (preco * 20 / 100), cor['cle']))
else:
    print('{}OPCAO INVALIDA{}.\nTente novamente'.format(cor['red'], cor['cle']))
