import time


def speed_calc_decorator(function):
    def wrapper_function():
        first_run = float(time.time())
        function()
        second_run = float(time.time())
        function()
        time_difference = second_run - first_run
        print(f"{time_difference}")

    return wrapper_function


@speed_calc_decorator
def slow_function():
    for x in range(0, 26):
        print(x)


@speed_calc_decorator
def fast_function():
    print("Hello World!")


slow_function()
fast_function()
