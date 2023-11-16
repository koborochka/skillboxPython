import functools
import logging
import datetime

logging.basicConfig(filename='function_errors.log', level=logging.ERROR)

def logging_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            error_message = f"Error in function '{func.__name__}': {str(e)}"
            logging.error(error_message)
            print(error_message)
    return wrapper


@logging_decorator
def example_function():
    print("Функция выполнена!")
    raise ValueError("Error occurred!")

@logging_decorator
def another_function():
    print("Еще одна функция выполнена!")

example_function()
another_function()
