def is_prime(number):
	divider_count = 0
	if number == 1 or number == 0:
		return False

	for divider in range(2, round(number**0.5+1)):
		if number % divider == 0:
			return False

	return True


def get_prime_element(object):
	result = []
	for index, item in enumerate(object):
		if is_prime(index):
			result.append(item)

	return result


print(get_prime_element([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(get_prime_element('О Дивный Новый мир!'))