import json


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
    Функция печатает через print все записи из файла records.json.

    EN:
    The function takes no arguments and returns None.
    The function prints all records from the file records.json using print.

    :return: None
    """

    with open('records.json', 'r', encoding='utf-8') as f:
        records = json.load(f)
        for n, record in enumerate(records, 1):
            formatted_record = json.dumps(record, ensure_ascii=False, indent=4)
            print(f'{n}. {formatted_record}')


def add_record():
    """
    RU:
    Функция не принимает аргументов и возвращает None.
    Функция добавляет в файл records.json новую запись.
    Вызывает функцию create_record.

    EN:
    The function takes no arguments and returns None.
    The function adds a new record to the file records.json.
    It calls the create_record function.

    :return: None
    """

    try:
        with open('records.json', 'r', encoding='UTF-8') as f:
            records = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        records: list = []

    new_record: dict = create_record()
    records.append(new_record)

    with open('records.json', 'w', encoding='UTF-8') as f:
        json.dump(records, f, indent=4, ensure_ascii=False)


def update_record():
    """
    RU:
    Функция не принимает аргументов и возвращает None.
    Функция редактирует запись в файле records.json по номеру записи.
    Вызывает функцию create_record.

    EN:
    The function takes no arguments and returns None.
    The function edits a record in the file records.json by the record number.
    It calls the create_record function.

    :return: None
    """

    with open('records.json', 'r', encoding='utf-8') as file:
        records = json.load(file)

        record_number = int(input('Введите номер записи которую хотите изменить: '))-1
        if 0 <= record_number < len(records):
            updated_data: dict = create_record(records[record_number])
            records[record_number].update(updated_data)
            with open('records.json', 'w', encoding='utf-8') as file:
                json.dump(records, file, ensure_ascii=False, indent=4)
            print("Запись успешно обновлена.")
        else:
            print("Запись с таким номером не найдена.")



def scan_recors():
    """
    RU:
    Функция не принимает аргументов и возвращает None.
    Функция запрашивает у пользователя через input параметры и значения для этих параметров,
    затем печатает через print все записи из файла records.json которые соответствуют параметрам.

    EN:
    The function takes no arguments and returns None.
    The function prompts the user via input for parameters and their values,
    then prints all records from the file records.json that match the parameters.

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

    with open('records.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        filtered_records: list = []
        for record in data:
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
            formatted_record = json.dumps(record, ensure_ascii=False, indent=4)
            print(f'{n}. {formatted_record}')
    else:
        print('Такие записи не найдены.')






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
                   'sc': scan_recors
                   }
    while True:
        print('Выберите действие: показать все записи - [s] | добавить запись - [a] | редоктировать запись - [u] | поиск по характеристикам - [sc]')
        action: str = input().lower().strip()
        try:
            action_dict[action]()

        except KeyError:
            print('Введины некорекктные значения')

        print('\n'+'-'*80+'\n')


if __name__ == '__main__':
    main()
