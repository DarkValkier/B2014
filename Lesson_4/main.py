a = 4
b = 2


try:
    print(a / b)
except ZeroDivisionError:
    print(f'Делить на ноль нельзя!')
except Exception as error:
    print(f'Что-то пошло не так: {type(error)} {error}')
else:
    print('Исключений не было')
finally:
    print('Блок отработает в любом случае')

print('Конец программы')