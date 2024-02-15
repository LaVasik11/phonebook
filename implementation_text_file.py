import ast

def create_record(current_values: dict = None) -> dict:
    """
    RU:
    Функция может принимать словарь как аргумент. Функция возвращает словарь.
    Функция запрашивает у пользователя через input данные(name, surname, patronymic,
    name_organization, phone_work, phone_personal) собирает из них словарь и возвращает его.

    EN:
    The function can take a dictionary as an argument. Dictionary return function.
    The function prompts the user via input for data (name, surname, patronymic,
    name_organization, phone_work, phone_personal), collects them into a dictionary, and returns it.

    :return: Dictionary with user data.
    :rtype: dict
    """

    if current_values is None:
        current_values = {}

    name: str = input('Введите имя: ') or current_values.get("имя", "")
    surname: str = input('Введите фамилию: ') or current_values.get("фамилия", "")
    patronymic: str = input('Введите отчество: ') or current_values.get("отчество", "")
    name_organization: str = input('Введите название_организации: ') or current_values.get("название_организации", "")
    phone_work: str = input('Введите телефон_рабочий: ') or current_values.get("телефон_рабочий", "")
    phone_personal: str = input('Введите телефон_личный: ') or current_values.get("телефон_личный", "")

    record: dict = {
        "имя": name,
        "фамилия": surname,
        "отчество": patronymic,
        "название_организации": name_organization,
        "телефон_рабочий": phone_work,
        "телефон_личный": phone_personal
    }

    return record



def show_record():
    """
    RU:
    Функция не принимает аргументов и возвращает None.
    Функция печатает через print все записи из файла records.txt.

    EN:
    The function takes no arguments and returns None.
    The function prints all records from the file records.txt using print.

    :return: None
    """

    with open('records.txt', 'r', encoding='utf-8') as f:
        records = f.readlines()
        for n, record in enumerate(records, 1):
            print(n)
            d = ast.literal_eval(record)
            for key, value in d.items():
                print(f"{key}: {value}")
            print('-'*35)


def add_record():
    """
    RU:
    Функция не принимает аргументов и возвращает None.
    Функция добавляет в файл records.txt новую запись.
    Вызывает функцию create_record.

    EN:
    The function takes no arguments and returns None.
    The function adds a new record to the file records.txt.
    It calls the create_record function.

    :return: None
    """

    new_record: dict = create_record()

    with open('records.txt', 'a', encoding='UTF-8') as f:
        f.writelines('\n' + str(new_record))



def update_record():
    """
    RU:
    Функция не принимает аргументов и возвращает None.
    Функция редактирует запись в файле records.txt по номеру записи.
    Вызывает функцию create_record.

    The function takes no arguments and returns None.
    The function edits a record in the file records.txt by the record number.
    It calls the create_record function.

    :return: None
    """

    with open('records.txt', 'r', encoding='utf-8') as f:
        records = f.readlines()

    record_number = int(input('Введите номер записи которую хотите изменить: ')) - 1
    if 0 <= record_number < len(records):
        updated_data = create_record(ast.literal_eval(records[record_number].strip()))
        records[record_number] = str(updated_data)
        with open('records.txt', 'w', encoding='utf-8') as file:
            file.writelines(records)
        print("Запись успешно обновлена.")
    else:
        print("Запись с таким номером не найдена.")



def scan_recors():
    """
    RU:
    Функция не принимает аргументов и возвращает None.
    Функция запрашивает у пользователя через input параметры и значения для этих параметров,
    затем печатает через print все записи из файла records.txt которые соответствуют параметрам.

    EN:
    The function takes no arguments and returns None.
    The function prompts the user via input for parameters and their values,
    then prints all records from the file records.txt that match the parameters.

    :return: None
    """

    valid_data: bool = False
    characteristics_dict: dict = {'n': 'имя',
                                  's': 'фамилия',
                                  'p': 'отчество',
                                  'o': 'название_организации',
                                  'pw': 'телефон_рабочий',
                                  'pp': 'телефон_личный',
                                  }

    while not valid_data:
        print('Введите через пробел буквы что бы указать по каким критериям вы хотите искать записи')
        print('имя - [n] | фамилия - [s] | отчество - [p] | название организации - [o] | телефон рабочий - [pw] | телефон личный - [pp]')
        search_for: list = input().split()
        for i in search_for:
            if i not in ['n', 's', 'p', 'o', 'pw', 'pp']:
                print('Введины некорекктные значения')
            else:
                valid_data: bool = True

    user_inputs = {}
    for key in search_for:
        user_inputs[key] = input(f'{characteristics_dict[key]}: '.replace("_", " "))

    with open('records.txt', 'r', encoding='utf-8') as file:
        file_content = file.readlines()
        records = [ast.literal_eval(i) for i in file_content]

        filtered_records: list = []
        for record in records:
            match: bool = True
            for key in search_for:
                if user_inputs[key].lower() != record.get(characteristics_dict[key]).lower():
                    match: bool = False
                    break
            if match:
                filtered_records.append(record)

    if filtered_records:
        print("Найденные записи:")
        for n, record in enumerate(filtered_records, 1):
            d = ast.literal_eval(str(record).strip())
            for key, value in d.items():
                print(f"{key}: {value}")
            print('-' * 35)
    else:
        print('Такие записи не найдены.')



def delete_record():
    """
    RU:
    Функция не принимает аргументов и возвращает None.
    Функция удаляет запись из файла records.txt по её номеру.

    EN:
    The function takes no arguments and does not return None.
    Function for deleting a record from the Records.txt file by its number.

    :return: None
    """

    with open('records.txt', 'r', encoding='utf-8') as file:
        records = file.readlines()

        record_number = int(input('Номер какой записи вы хотите удалить?: '))-1
        if 0 <= record_number < len(records):
            del records[record_number]
            with open('records.txt', 'w', encoding='utf-8') as file:
                file.writelines(records)
            print("Запись успешно удаленна.")
        else:
            print("Запись с таким номером не найдена.")


def main():
    """
    RU:
    Функция не принимает аргументов и возвращает None.
    Функция Запрашивает у пользователя через input действие
    и в зависимости от его выбора вызывает другие функции.

    EN:
    The function takes no arguments and returns None.
    The function prompts the user via input for an action and depending on their choice,
    calls other functions.

    :return: None
    """
    action_dict: dict = {'s': show_record,
                         'a': add_record,
                         'u': update_record,
                         'sc': scan_recors,
                         'd': delete_record
                         }
    while True:
        print('Выберите действие: показать все записи - [s] | добавить запись - [a] | редоктировать запись - [u] | поиск по характеристикам - [sc]')
        action: str = input().lower().strip()
        try:
            action_dict[action]()

        except KeyError:
            print('Введины некорекктные значения')

        print('\n'+'#'*130+'\n')


if __name__ == '__main__':
    main()
