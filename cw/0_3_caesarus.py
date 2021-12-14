import time

def caesarus_encode(text: str, shift: int) -> str:
    """
    Функция шифрует текст шифром Цезаря. Смысл заключается в том что коды
    символов сдвигаются, что осуществляет обратимое преобразование. Если
    упростить до реализации, то необходимо преобразовать символ в число,
    прибавить сдвиг и преобразовать результат обратно в символ, и таким
    образом обработать весь текст.

    Функции chr и ord позволяют преобразовывать код (целое число от 0 до 2^16
    (2^8)) в символ и наоборот.

    :param text: исходный текс
    :return: преобразованный текст
    """
    result = ""
    for s in text:
        result += chr(ord(s) + shift)
    return result

def caesarus_decode(text: str, shift: int) -> str:
    result = ""
    for s in text:
        result += chr(ord(s) - shift)
    return result


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
    text = "Митинг в 13:30 на болотной"
    shift = 11
    result = "Чуэушо+н+<>E>;+шл+мщцщэшщф"

    test_function(caesarus_encode, result, text, shift)

    text = "Митинг в 13:30 на болотной"
    shift = 532
    result = "ذٌٌّٖهȴنȴɅɇɎɇɄȴّلȴمٍُّْْْٖ"

    test_function(caesarus_encode, result, text, shift)



if __name__ == "__main__":
    test()
