from utils.bcolor import *


def print_func_name_before_and_after_execution(func):
    def wrap(*args, **kwargs):
        print_green(f"function name before execution: {func.__name__}")
        result_temp = func(*args, **kwargs)
        print_green(f"function name after execution: {func.__name__}")
        return result_temp

    return wrap


def print_func_name_before_execution(func):
    def wrap(*args, **kwargs):
        print_header(f"function name before execution ONLY: {func.__name__}")
        return func(*args, **kwargs)

    return wrap


@print_func_name_before_execution
@print_func_name_before_and_after_execution
def greet(user):
    print(f"Hello {user}!")
    return "end"


greet("Jack")
