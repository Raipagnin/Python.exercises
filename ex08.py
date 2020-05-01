# escreva um programa que leia um valor em metros e o exiba convertido em cm e mm
n = float(input('Digite sua metragem: '))
cm = n*100
mm = n*1000
print('{}m eh igual a {:.0f}cm e {:.0f}mm'.format(n, cm, mm)) # :.0f arredonda!

