import functools


def how_are_you(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        how_are_you_response = input("Как дела? ")
        print(f"А у меня не очень! Ладно, держи свою функцию.")
        return func(*args, **kwargs)

    return wrapper


@how_are_you
def test():
    print('<Тут что-то происходит...>')

test()
