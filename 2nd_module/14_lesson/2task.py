import time
import functools

def delay_decorator(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Ждем {seconds} секунд...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@delay_decorator(3)
def example_function():
    print("Функция выполнена!")

example_function()
