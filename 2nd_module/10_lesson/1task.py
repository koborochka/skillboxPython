line_number = 0
names_length = 0
error_log = []
try:
	with open("people.txt", "r", encoding="utf-8") as people_file:
		for i_line in people_file:
			if i_line.endswith("\n"):
				i_line = i_line.strip()

			line_number += 1

			try:
				if len(i_line) >= 3:
					names_length += len(i_line)
				else:
					names_length += len(i_line)
					error_message = ("Ошибка: менее трёх символов в строке {}.".format(line_number))

					raise ValueError(error_message)
			except ValueError:
				error_log.append(error_message)
				print(error_message)

except FileNotFoundError:
	print("Такого файла не существует")
finally:
	with open("errors.log", "w", encoding="utf-8") as error:
		error.write("\n".join(error_log))
	print("Общее количество символов: {}".format(names_length))