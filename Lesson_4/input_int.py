def input_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print('Вы ввели некорректное значение!')
            print('Попробуйте ещё раз.')


a = input_int('Введите a:')
b = input_int('Введите b:')

print(a + b)