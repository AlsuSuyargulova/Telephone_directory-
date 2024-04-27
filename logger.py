from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберете вариант: ")) 

    while var != 1 and var !=2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    if var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n")


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = 1
        print(''.join(data_first_list))

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)


def update_data():
    print("Выберите вариант файла: \n 1 - вариант списком \n 2 - вариант строчный")
    var = int(input('Введите вариант: '))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    search_text = str(input(f"Введите данные для обновления: "))  
    updated_text = str(input(f"Введите новые данные: "))
    updated = False

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()

        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for line in data:
                if search_text in line:
                    f.write(line.replace(search_text, updated_text))
                    updated = True
                else:
                    f.write(line)
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()

        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for line in data:
                if search_text in line:
                    f.write(line.replace(search_text, updated_text))
                    updated = True
                else:
                    f.write(line)

    if updated:
        print(f"Данные '{search_text}' успешно обновлены на '{updated_text}'.")
    else:
        print(f"Данные с '{search_text}' не найдены в файле.")
                    

def delete_data():
    print("Выберите вариант файла: \n 1 - вариант списком \n 2 - вариант строчный")
    var = int(input('Введите вариант: '))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    search_text = str(input(f"Введите данные для удаления: "))  
    deleted = False

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()

        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for line in data:
                if search_text not in line:
                    f.write(line)
                else:
                    deleted = True
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()

        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for line in data:
                if search_text not in line:
                    f.write(line)
                else:
                    deleted = True

    if deleted:
        print(f"Данные с '{search_text}' успешно удалены из файла.")
    else:
        print(f"Данные с '{search_text}' не найдены в файле.")
