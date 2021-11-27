def different_in_row(text: str) -> int:
    """
    Функция находит максимальное количество идущих подряд **различных** символов.
    Различными должны быть только соседние символы.

    :param text: Анализируемый текст
    :return: Максимальное количество идущих подряд **различных** символов
    """
    pass

class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def test_different_in_row(text, result):
    test_result = different_in_row(text)
    check = test_result == result
    if len(text) > 100:
        text = text[:45] + " ... " + text[-45:]
    print("text =", text)
    print(f"result = {result}; test_result = {test_result}")
    print(f"{bcolors.OK}Test passed{bcolors.ENDC}" if check else f"{bcolors.FAIL}Test failed{bcolors.ENDC}")


def test():
    text = "Привет!"
    result = 7
    test_different_in_row(text, result)

    text = "Доббрый вечер!"
    result = 11
    test_different_in_row(text, result)

    text = "ггаывалоРВГаргыватвмсцшвавыраррывпаллллывароимгсвггвНННВаыттвттавоооООооооооВЫвыва"
    result = 29
    test_different_in_row(text, result)

    text = "Ф"*1000
    result = 1
    test_different_in_row(text, result)


if __name__ == "__main__":
    test()
