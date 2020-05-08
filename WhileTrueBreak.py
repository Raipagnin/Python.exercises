#while true/break
s = 0
while True: # nao precisa colocar gambiarra de n = 0 antes de while
    n = int(input('Digite um numero [999] pra parar: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s)) #uso de f strings apos python 3.6
print(f'A soma vale {s}') # nova maneira 
