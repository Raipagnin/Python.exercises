while True:
    n = int(input('tabuada de qual numero deseja ver?: '))
    if n < 0:
        break
    print('-'*20)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('FIM')
