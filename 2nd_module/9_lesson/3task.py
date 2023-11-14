import os

dir_count = 0
files_count = 0
size = 0
path = os.path.abspath(input("Введите путь до каталога: "))

if os.path.exists(path):
	if os.path.isdir(path):
		for files in os.listdir(path):
			if os.path.isdir(files):
				dir_count += 1
				size += os.path.getsize(os.path.join(path, files))
			else:
				files_count += 1
				size += os.path.getsize(os.path.join(path, files))
		print("{} - кол-во подкаталогов, {} - кол-во файлов, {} КБ - размер файлов".format(dir_count, files_count, size / 1024))
	else:
		print("Это файл и его размер {}Кб".format(os.path.getsize(path) / 1024))
else:
	print("Такого пути не существует")