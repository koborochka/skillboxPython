class SquareIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        else:
            result = self.current ** 2
            self.current += 1
            return result


def square_generator(limit):
    current = 1
    while current <= limit:
        yield current ** 2
        current += 1


def square_expression(limit):
    return (i ** 2 for i in range(1, limit + 1))


limit = int(input("Введите число N: "))
if limit <= 0:
    raise ValueError("Введите положительное число.")

print("Итератор:")
square_iter = SquareIterator(limit)
for num in square_iter:
    print(num, end=" ")
print("\n")

print("Генератор:")
for num in square_generator(limit):
    print(num, end=" ")
print("\n")

print("Генераторное выражение:")
for num in square_expression(limit):
    print(num, end=" ")
print("\n")
