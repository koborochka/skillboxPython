import time


class LoggerDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Вызов функции {self.func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")

        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()

        print(f"Результат: {result}")
        print(f"Время выполнения: {end_time - start_time} секунд")

        return result


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


result = complex_algorithm(10, 50)
