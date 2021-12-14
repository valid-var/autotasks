import time

def power(x: int, y: int):
    """
    Данная функция производит операцию возведения в степень над целыми
    числами используя рекурсивный алгоритм.

    :param x: целочисленное основание степени
    :param y: целочисленный показатель степени
    :return: результат возведения в степень
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
    x = 2
    y = 2
    result = 4
    test_function(power, result, x, y)

    x = 2
    y = 3
    result = 8
    test_function(power, result, x, y)

    x = 6
    y = 2
    result = 36
    test_function(power, result, x, y)

    x = 1
    y = 100
    result = 1
    test_function(power, result, x, y)

    x = 2
    y = -1
    result = 0.5
    test_function(power, result, x, y)


if __name__ == "__main__":
    test()
