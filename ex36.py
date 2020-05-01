# emprestimo de casa, peca valor da casa, salario mensal, em qtos anos quer pagar, e a prestacao mensal nao pode exceder 30%do sal mensal
cor = {'cle': '\033[m', 'red': '\033[1;31m', 'gre': '\033[1;32m', 'yel': '\033[4;33m', 'blu': '\033[1;34m'}
home = float(input('What\'s the price of the house? $ '))
sal = float(input('What\'s the monthly salary? $ '))
year = int(input('In how many years would you like to pay the total amount? '))
parcel = home / (12 * year)
sal1 = sal * 30 / 100
if sal1 >= parcel:
    print('The installment on the house will be {}{:.2f}{} monthly, therefore, based on your salary\nWhere {}30%{} doesn\'t '
          'surpass the monthly pay.{}YOU CAN HAVE A LOAN!{}'.format(cor['blu'], parcel, cor['cle'], cor['yel'], cor['cle'],
                                                                               cor['gre'], cor['cle']))
else:
    print('The installment on the house will be {}{:.2f}{} monthly, therefore, based on your salary\nWhere {}30%{} exceeds'
          ' the limit on your monthly limit, being: {}{:.2f}{}!.\n{}I\'M SORRY!{}\n{}LOAN DECLINED!{}'.format(cor['blu'], parcel, cor['cle'],
                                                                                          cor['yel'], cor['cle'], cor['red'],
                                                                                          sal1, cor['cle'], cor['yel'], cor['cle'],
                                                                                          cor['red'], cor['cle']))




