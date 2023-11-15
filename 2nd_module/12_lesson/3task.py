class MyDict(dict):
	def get(self, key, default=0):
		return super().get(key, default)


my_dict = MyDict({'q': 1, 'w': 2})

print(my_dict.get('e'))  # Вывод: 0
print(my_dict.get('q'))  # Вывод: 1
print(my_dict.get('w'))  # Вывод: 2