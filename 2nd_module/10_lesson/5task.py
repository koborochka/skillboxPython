import math


def calculate_square_root(number):
	try:
		if number <= 0:
			raise ValueError("Из этого числа невозможно взять корень")
		result = f"Квадратный корень числа {number} равен {math.sqrt(number)}"

	except ValueError as ve:
		return f"Ошибка: {ve}"
	except Exception as e:
		return f"Произошла ошибка: {e}"
	else:
		return result

try:
	number = float(input("Введите число: "))
	result = calculate_square_root(number)
	print(result)
except ValueError:
	print("Вы ввели неправильные данные")