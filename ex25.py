#verifique se existe Silva dentro de um nome completo/frase
name = str(input('Digite seu nome completo: ')).upper().strip().split()
print('Existe "Silva" no seu nome?: {}'.format('SILVA'in name))

