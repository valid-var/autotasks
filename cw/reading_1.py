import time


def stranger_function(stranger_value):
    assert stranger_value >= 0, "Operation not possible"
    if stranger_value > 1:
        return stranger_value * stranger_function(stranger_value - 1)
    else:
        return 1


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
    input_value = 2
    # start_time = time.time()
    result = 2
    # end_time = time.time() - start_time
    # print(f"MATH TIME = {end_time}")
    test_function(stranger_function, result, input_value)

    input_value = 21
    # start_time = time.time()
    result = 51090942171709440000
    # end_time = time.time() - start_time
    # print(f"MATH TIME = {end_time}")
    test_function(stranger_function, result, input_value)

    input_value = 210
    # start_time = time.time()
    result = 105823620292236563784274284243348353057589905787169019562352737522144487532400210147849369011714673954768265316577892528273760626189481169051055226066650741189573897273684791411180134039439160066561895838501000817711682625725670477616267598661259194975646029749546282594356217374097544153589482020891750774735012558313460846824864172030239122128896000000000000000000000000000000000000000000000000000
    # end_time = time.time() - start_time
    # print(f"MATH TIME = {end_time}")
    test_function(stranger_function, result, input_value)


if __name__ == "__main__":
    test()
