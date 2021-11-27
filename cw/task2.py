
def mean(A: list) -> int:
    """
    Функция считает среднее арифмитическое элементов списка.
    Результат округляется до целого **в большую сторону**.
    Допускается использовать функцию округления из модуля math.

    :param A: список чисел
    :return: результат среднего арифметического округленный в большую сторону
    """
    pass


class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'


def test_mean(A, result):
    test_result = mean(A)
    check = test_result == result
    if len(A) > 10:
        A = A[:5] + ["..."] + A[-5:]
    print("A =", A)
    print(f"result = {result}; test_result = {test_result}")
    print(f"{bcolors.WARNING}Wrong type{bcolors.ENDC}" if type(test_result) != type(result) else f"Type check passed")
    print(f"{bcolors.OK}Test passed{bcolors.ENDC}" if check else f"{bcolors.FAIL}Test failed{bcolors.ENDC}")


def test():
    A = [1, 2, 3, 4, 5]
    result = 3
    test_mean(A, result)

    A = [3, 3, 3, 3, 3, 1]
    result = 3
    test_mean(A, result)

    A = [3.9, 3.5, 6.9, 3.3, 3.99, 1.06]
    result = 4
    test_mean(A, result)

    A = list(range(0, 10000))
    result = 5000
    test_mean(A, result)


if __name__ == "__main__":
    test()
