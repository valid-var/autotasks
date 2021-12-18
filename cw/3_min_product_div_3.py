import time


def min_product_div_3(pair_list: list) -> int:
    """
    Нужно выбрать из каждой пары число для произведения так, чтобы
    итоговое произведение делилось на 3 и было наименьшим.
    Числа не больше 25000

    :param pair_list: Список пар чисел
    :return: Наименьшее произведение, делящееся на 3, или -1
    """
    product = 1
    return product


class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def test_function(function, result, *input_values):
    start_time = time.time()
    test_result = function(*input_values)
    end_time = time.time() - start_time
    check = test_result == result
    print(f"input values: ", "; ".join([str(value) for value in input_values]))
    print(f"true result = {result}; test result = {test_result}; TIME = {end_time}")
    print(f"{bcolors.OK}Test passed{bcolors.ENDC}" if check else f"{bcolors.FAIL}Test failed{bcolors.ENDC}")


def test():
    input_value = [[1, 2], [100, 23], [20, 33]]
    result = 759
    test_function(min_product_div_3, result, input_value)

    input_value = [[9, 2], [100, 23], [20, 33]]
    result = 1518
    test_function(min_product_div_3, result, input_value)

    input_value = [[1, 2], [100, 23], [20, 11]]
    result = -1
    test_function(min_product_div_3, result, input_value)



if __name__ == "__main__":
    test()
