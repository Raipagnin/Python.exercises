#faca um algoritimo que leia o preco de um produto e mostre seu novo preco com 5% de desconto

n = float(input('Digite preco do produto: '))
d = n - (5*n/100)
print('No valor {},\nPreco final eh {:.2f}'.format(n, d))
