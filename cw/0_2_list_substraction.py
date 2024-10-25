import time

def list_addition(A: list, B: list) -> list:
    """
    Функция складывает списки A и B поэлементно.

    :param A: список целых чисел
    :param B: список целых чисел
    :return: список целых чисел
    """
    pass

def list_2d_addition_indexes(A: list, a: int, b: int) -> list:
    """
    Дана матрица NxN А вида [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
    Необходимо найти сумму строк по индексам a и b.

    :param A: двумерный список
    :param a: индекс первой строки
    :param b: индекс второй строки
    :return: список целых чисел
    """
    return list_addition(A[a], A[b])

def list_2d_addition(A: list) -> list:
    """
    Дана матрица NxN А вида [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
    Необходимо найти сумму всех строк поэлементно.

    :param A: двумерный список
    :return: список целых чисел
    """
    pass

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
    B = [0, 2, -3, -1, 3]
    result = [1, 4, 0, 3, 8]

    test_function(list_addition, result, A, B)

    A = [1, 2, 3, 4, 5, 6, 7]
    B = [0, 2, -3, -1, 3]
    result = [1, 4, 0, 3, 8, 6, 7]

    test_function(list_addition, result, A, B)

    A = [[4, 2, 4, 1], [1, -2, 3, 5], [2, -1, 4, -5], [3, 6, 5, 1]]
    a, b = 0, 3
    result = [7, 8, 9, 2]

    test_function(list_2d_addition_indexes, result, A, a, b)

    A = [[4, 2, 4, 1], [1, -2, 3, 5], [2, -1, 4, -5], [3, 6, 5, 1]]
    result = [10, 5, 16, 2]

    test_function(list_2d_addition, result, A)


if __name__ == "__main__":
    test()
