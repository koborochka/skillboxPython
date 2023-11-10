contacts = {}

while True:
	action = input("Введите номер действия \n(1)Добавить контакт \n(2) Найти человека: ").lower()

	if action == "1":
		name, surname = input("Введите имя и фамилию нового контакта (через пробел): ").split()
		phone = input("Введите номер телефона: ")
		if (name, surname) in contacts:
			print("Такой человек уже есть в контактах.")
		else:
			contacts[(name, surname)] = phone
			print("Текущий словарь контактов:", contacts)

	elif action == "2":
		surname_to_find = input("Введите фамилию для поиска: ").capitalize()
		found_contacts = {f"{name} {surname}": phone for (name, surname), phone in contacts.items() if
						  surname.lower() == surname_to_find.lower()}
		if found_contacts:
			for contact, phone in found_contacts.items():
				print(contact, phone)
		else:
			print("Контакт с такой фамилией не найден.")

	else:
		print("Некорректное действие. Попробуйте снова.")