# guess even or odd. u play a number and the computer plays another one, the addition becomes the answer(even or odd)
from random import randint
from time import sleep
print('-='*30)
print('LET\'S PLAY EVEN OR ODDS')
print('-='*30)
c = 0
while True:
    pl = int(input('Type a number 0-10  : '))
    pc = randint(0, 10)
    add = pl + pc
    guess = ' '
    while guess not in 'EO':
        guess = str(input('Guess if even or odd [E/O]: ')).strip().upper()[0]
    print('-' * 30)
    print(f'You\'ve played {pl} and the pc {pc}. TOTAL = {add}')
    print('-' * 30)
    if guess == 'E':
        if add % 2 == 0:
            print('YOU WIN!!\nLET\'S PLAY AGAIN')
            c += 1
        else:
            print('GAME OVER')
            break
    if guess == 'O':
        if add % 2 == 1:
            print('YOU WIN!!\nLET\'S PLAY AGAIN')
            c +=1
        else:
            print('GAME OVER')
            break
print(f'YOU WON {c} times')
# could have dropped a few lines using 'or', but better looking this way*easier?
