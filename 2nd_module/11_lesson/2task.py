class Student:

	def __init__(self, name, surname, group_number, estimation):
		self.name = name
		self.surname = surname
		self.group_number = group_number
		self.estimation = estimation

	def info(self):
		print("Имя и фамилия студента: {0} {1} Номер группы: {2} Оценки студента: {3}".format(self.name, self.surname,
																								self.group_number,
																								self.estimation))

	def get_average(self):
		estimate_count = 0
		score = 0
		for estimation in self.estimation:
			score += estimation
			estimate_count += 1

		return score / estimate_count

ivan = Student("Иван", "Семенов", "РИ-100001", [4, 3, 3, 4, 5])
natalia = Student("Наталья", "Иванова", "РИ-100002", [5, 4, 5, 4, 4])
pavel = Student("Павел", "Козлов", "РИ-100003", [5, 4, 3, 4, 5])
yulia = Student("Юлия", "Петрова", "РИ-100004", [5, 5, 5, 5, 5])
maxim = Student("Максим", "Сидоров", "РИ-100005", [4, 4, 3, 5, 4])
alex = Student("Алексей", "Иванов", "РИ-123456", [4, 5, 4, 3, 5])
marina = Student("Марина", "Смирнова", "РИ-234567", [5, 4, 4, 5, 5])
nikita = Student("Никита", "Петров", "РИ-345678", [3, 2, 3, 3, 2])
olga = Student("Ольга", "Козлова", "РИ-456789", [5, 4, 5, 5, 4])
dmitry = Student("Дмитрий", "Соколов", "РИ-567890", [4, 5, 3, 2, 5])

students = [alex, marina, nikita, olga, dmitry, ivan, natalia, pavel, yulia, maxim]
for i in range(len(students) - 1):
	for j in range(i + 1, len(students)):
		if students[i].get_average() < students[j].get_average():
			temp = students[i]
			students[i] = students[j]
			students[j] = temp

print("После сортировки: ")
for i in students:
	i.info()
	print(("Средний балл: {0}".format(i.get_average())))