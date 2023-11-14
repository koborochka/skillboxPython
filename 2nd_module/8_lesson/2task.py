def find_key(structure, my_key, depth=100):
	if depth is None or depth >= 1:
		if my_key in structure:
			return structure[my_key]
	else:
		return None
	for element in structure.values():
		if isinstance(element, dict):
			result = find_key(element, my_key, depth - 1)
			if result:
				break
	else:
		result = None
	return result


site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}
key = input('Введите искомый ключ: ')

yes_or_no = input("Хотите ввести максимальную глубину? Y/N: ").lower()
if yes_or_no == 'y':
	maximum_depth = int(input('Введите максимальную глубину: '))
	value_key = find_key(site, key, maximum_depth)
else:
	value_key = find_key(site, key)
print(f'Значение ключа: {value_key}')