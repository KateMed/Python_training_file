import random

max=100
count=0;
n=random.randint(1,max)
a='Да введите вы уже число! '
b='Число! '
c='Мне от тебя нужно только число! Снова и снова! '
d='Вы уже так близки к победе, здесь становится горячо!'
print(f'Это игра! Числа в диапазоне 1 : {max}, для выхода введите exit')
while True:

    inp=input(random.choice([a,b,c,d]))
    if inp=='exit':
        print('Вы вышли из игры. До скорых встреч!')
        break
    elif not inp.isdigit():
        print('Я же попросил тебя вводить число, игра не работает иначе!')
        continue

    inp = int(inp)
    if inp>n:
        print('Ваше число слишком большое')
        count=count+1
    elif inp<n:
        print('Ваше число слишком маленькое')
        count = count + 1
    else:
        count = count + 1
        print(f'Это победа! Вы угадали c {count} попытки!')
        break