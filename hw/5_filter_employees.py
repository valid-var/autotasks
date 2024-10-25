"""
Вы разрабатываете систему управления данными о сотрудниках для компании. Данные представлены в виде вложенных списков с различными типами данных.
Условия задачи:

    Напишите функцию, которая принимает список данных о сотрудниках.

    Каждый элемент списка данных о сотрудниках представлен как подсписок, который включает:
        name (str): имя сотрудника.
        age (int): возраст сотрудника.
        salary (float): заработная плата сотрудника.
        department (str): отдел, в котором работает сотрудник.

    Пример данных:

employees_data = [
    ["Alice", 30, 50000.0, "Engineering"],
    ["Bob", 24, 45000.0, "Sales"],
    ["Carol", 29, 70000.0, "Engineering"],
    ["Dave", 35, 52000.0, "Sales"],
    ["Eve", 40, 60000.0, "HR"]
]

Функция должна:

    Отфильтровать сотрудников, которые работают в отделе "Engineering" и имеют зарплату выше threshold (пороговое значение заработной платы, передаваемое параметром).
    Вернуть новый список, в котором каждая запись — это строка, представляющая имя и возраст сотрудника из отфильтрованного списка.
"""

def filter_employees(employees_data: list, threshold: float) -> list:
    """
    Фильтрует сотрудников по заданным критериям.

    Параметры:
    - employees_data (list): Вложенный список, где каждый элемент — подсписок с данными о сотруднике
                             в формате [name (str), age (int), salary (float), department (str)].
    - threshold (float): Пороговое значение зарплаты для фильтрации сотрудников из отдела "Engineering".

    Возвращает:
    - list: Список строк, где каждая строка содержит имя и возраст сотрудников, прошедших фильтрацию.
    """
    pass


class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def test_filter_employees(employees_data, threshold, expected_result):

    # Вызов функции
    result = filter_employees(employees_data, threshold)

    # Проверка результатов
    assert result == expected_result, f"Ожидалось: {expected_result}, Получено: {result}"


def test():
    employees_data = [
        ["Alice", 30, 50000.0, "Engineering"],
        ["Bob", 24, 45000.0, "Sales"],
        ["Carol", 29, 70000.0, "Engineering"],
        ["Dave", 35, 52000.0, "Sales"],
        ["Eve", 40, 60000.0, "HR"]
    ]

    # Ожидаемые результаты
    threshold = 55000.0
    expected_result = [
        "Carol, 29"
    ]

    test_filter_employees(employees_data, threshold, expected_result)
    print(f"{bcolors.OK}Все тесты пройдены.{bcolors.ENDC}")


if __name__ == "__main__":
    test()
