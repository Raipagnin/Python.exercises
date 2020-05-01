#pedindo 3 retas, calculando se pode formar um triangulo, e que tipo de triangulo
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
if a < b + c and b < a + c and c < a + b:
    print('As medidas acima PODEM formar um triangulo', end=' ')
    if a == b and b == c: # vc tb pode colocar a == b == c
        print('EQUILATERO')
    elif a != b != c != a: #enquanto a igualdade pode ser inclusiva, a diferenca nao. se colocar a != b != c
        print('ESCALENO')                #nao funciona, pois a pode ser == c
    else:
        print('ISOSCELES') # por ser o triangulo mais longo de se descrever, melhor deixar por ultimo como else
else:
    print('Essas medidas NAO podem formar um triangulo')
