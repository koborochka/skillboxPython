from functools import wraps
from datetime import datetime

def log_methods(date_format):
    def decorator(cls):
        class Wrapper(cls):
            def __getattribute__(self, name):
                attr = super().__getattribute__(name)
                if callable(attr):
                    return self._wrap_method(attr, name)
                return attr

            def _wrap_method(self, method, name):
                @wraps(method)
                def wrapper(*args, **kwargs):
                    start_time = datetime.now()
                    formatted_date = start_time.strftime(date_format)
                    print(f"Запускается '{cls.__name__}.{name}'. Дата и время запуска: {formatted_date}.")

                    result = method(*args, **kwargs)

                    end_time = datetime.now()
                    elapsed_time = end_time - start_time
                    print(f"Завершение '{cls.__name__}.{name}', время работы = {elapsed_time.total_seconds():.3f} s.")

                    return result

                return wrapper

        return Wrapper

    return decorator

@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1.')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника.")

    def test_sum_2(self):
        print("Тут метод test_sum_2 у наследника.")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
