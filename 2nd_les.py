#name = input('Как тебя зовут?')
age = int (input('Сколько тебе лет?'))

if age >= 0:
    if age < 18:
        print('Вам еще нет 18')
    else:
        print('Добро пожаловать!')
else:
    print('Некорректный возраст')
