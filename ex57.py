#pergunte sexo da galera e so aceite S ou M, nao deixe passar pra proxima pergunta
s = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0] #esse zero eh so pra pegar a primeira letra caso coloce "masculino" "Mn"
while s not in 'MF':
    s = str(input('Dados invalidos. Digite seu sexo [F/M]: ')).strip().upper()[0]
print('sexo {} registrado'.format(s))



