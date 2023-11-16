import functools


def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Функция {func.__name__} была вызвана {wrapper.calls} раз(а).")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper



@counter
def example_function():
    print("Это пример функции.")


@counter
def another_function():
    print("Еще одна функция.")


example_function()
example_function()
another_function()
