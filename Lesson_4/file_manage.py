while True:
    file_name = input('Введите название файла:')

    print(f'Открываем файл {file_name}...')
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print('Файл не найден!')
        answer = input('Хотите ввести название ещё раз? (y/n):')
        if answer == 'n':
            break
    else:
        print('Содержимое файла:')
        for line in file.readlines():
            print(line.strip('\n'))

        file.close()
        break
