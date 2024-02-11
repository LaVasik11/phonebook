
# Программа управления записями
## Эта программа предоставляет возможность создавать, просматривать, обновлять и искать записи в файле records.json.

### Инструкции по использованию
Запустите программу, выполнив файл main.py.
Следуйте инструкциям ввода для выполнения необходимых действий.
Доступные действия
Показать все записи: Выберите эту опцию, чтобы просмотреть все записи из файла records.json.
Добавить запись: Добавьте новую запись в файл records.json, предоставив запрашиваемые данные.
Редактировать запись: Выберите эту опцию, чтобы обновить существующую запись, указав номер записи и предоставив новые данные.
Поиск по характеристикам: Ищите записи по различным критериям, таким как имя, фамилия, название организации и т.д.
Функции
create_record()
Создает новую запись, запрашивая данные у пользователя через ввод и возвращает словарь с этими данными.


## Функции:

1. ### show_record()
    Выводит все записи из файла records.json.

2. ### add_record()
    Добавляет новую запись в файл records.json, вызывая функцию create_record().

3. ### update_record()
    Редактирует существующую запись в файле records.json по номеру записи, вызывая функцию create_record().

4. ### scan_records()
    Позволяет пользователю искать записи в файле records.json по различным характеристикам.

5. ### main()
    Основная функция программы, которая предоставляет пользователю выбор доступных действий и вызывает соответствующие функции в зависимости от выбора пользователя.


## Требования к выполнению
Python 3.x
Файл records.json, в котором хранятся записи, должен находиться в том же каталоге, что и main.py.


## Зависимости
json: Для работы с JSON-файлами.
Замечания
При редактировании записи номер указывается с учетом индексации с единицы, а не с нуля.
Все операции с записями в файле records.json производятся в кодировке UTF-8.
