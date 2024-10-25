"""
Необходимо посчитать, сколько раз каждый товар упоминается в строке и определить общую стоимость всех упомянутых товаров.
Условия задачи:

    Напишите функцию, которая принимает следующие параметры:
        product_string (str): строка с названиями товаров, разделёнными запятыми (например, "apple,banana,orange,apple,banana").
        prices (dict): словарь с названиями товаров и их ценами (например, {"apple": 1.0, "banana": 0.5, "orange": 1.2}).

    Функция должна:
        Посчитать количество каждого товара в product_string и вернуть его в виде словаря name_count.
        Вычислить общую стоимость всех упомянутых товаров по ценам из prices и вернуть её как total_cost.
"""

def analyze_purchases(product_string: str, prices: dict) -> tuple:
    """
    Анализирует список покупок.

    Параметры:
    - product_string (str): Строка с названиями товаров, разделёнными запятыми.
    - prices (dict): Словарь, содержащий названия товаров и их цены.

    Возвращает:
    - tuple: кортеж из двух элементов:
      - name_count (dict): Словарь с количеством каждого товара.
      - total_cost (float): Общая стоимость всех товаров.
    """
    pass

class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def test_analyze_purchases(product_string, prices, expected_name_count, expected_total_cost):

    # Вызов функции
    name_count, total_cost = analyze_purchases(product_string, prices)

    # Проверка результатов
    assert name_count == expected_name_count, f"Ожидалось: {expected_name_count}, Получено: {name_count}"
    assert abs(total_cost - expected_total_cost) < 1e-6, f"Ожидалось: {expected_total_cost}, Получено: {total_cost}"

def test():
    # Данные для тестов
    product_string = "apple,banana,orange,apple,banana"
    prices = {
        "apple": 1.0,
        "banana": 0.5,
        "orange": 1.2
    }

    # Ожидаемые результаты
    expected_name_count = {
        "apple": 2,
        "banana": 2,
        "orange": 1
    }
    expected_total_cost = (1.0 * 2) + (0.5 * 2) + (1.2 * 1)  # 2 + 1 + 1.2 = 4.2

    test_analyze_purchases(product_string, prices, expected_name_count, expected_total_cost)
    print(f"{bcolors.OK}Все тесты пройдены.{bcolors.ENDC}")


if __name__ == "__main__":
    test()
