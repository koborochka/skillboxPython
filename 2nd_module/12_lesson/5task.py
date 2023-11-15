class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()


class TaskManager:
	def __init__(self):
		self.tasks = Stack()

	def new_task(self, task, priority):
		self.tasks.push((task, priority))

	def __str__(self):
		sorted_tasks = sorted(self.tasks.items, key=lambda x: x[1])
		result = ""
		prev_priority = None
		for task in sorted_tasks:
			if task[1] != prev_priority:
				if prev_priority is not None:
					result = result[:-2] + "\n"
				result += f"{task[1]} - {task[0]}, "
				prev_priority = task[1]
			else:
				result += f"{task[0]}, "
		return result[:-2]


manager = TaskManager()

manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)

print(manager)