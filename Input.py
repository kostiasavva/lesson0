from itertools import cycle

name = input('Как вас зовут? ')
while True:
    age = input('Введите ваш возраст: ')
    try: age = int(age)
    except ValueError:
        print('Введите корректное число лет!')
        continue
    else: print(f'{name}, через пять лет вам будет {age + 5}.')
    break
