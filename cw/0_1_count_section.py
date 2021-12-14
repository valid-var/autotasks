import time

def count_section(A: list, a: int, b: int) -> int:
    """
    Функция находит все элементы, принадлежащие заданному промежутку [a,b]

    :param A: список целых чисел
    :param a: целое число, начало промежутка
    :param b: целое число, конец промежутка
    :return: количество элементов принадлежащих [a,b]
    """
    k = 0
    for elem in A:
        if a <= elem <= b or a >= elem >= b:
            k += 1
    return k

def return_section(A: list, a: int, b: int) -> list:
    """
    Функция находит все элементы, принадлежащие заданному промежутку [a,b)

    :param A: список целых чисел
    :param a: целое число, начало промежутка
    :param b: целое число, конец промежутка
    :return: список элементов принадлежащих [a,b)
    """
    B = []
    for elem in A:
        if a <= elem < b or a >= elem > b:
            B.append(elem)
    return B


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
    A = [1, 2, 3, 4, 5]
    a = 3
    b = 6
    result = 3

    test_function(count_section, result, A, a, b)

    A = [-1, -2, -3, -4, -5]
    a = 3
    b = 6
    result = 0

    test_function(count_section, result, A, a, b)

    A = [-1, -2, -3, -4, -5]
    a = -1
    b = -3
    result = 3

    test_function(count_section, result, A, a, b)

    A = [-1, -2, 3, -4, -5]
    a = -3
    b = 0
    result = 2

    test_function(count_section, result, A, a, b)



if __name__ == "__main__":
    test()
