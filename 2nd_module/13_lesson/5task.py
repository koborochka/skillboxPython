import os

def error_log_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                yield line

def filter_errors(input_file):
    with open("errorLog.txt", 'w') as out_file:
        for error_line in error_log_generator(input_file):
            out_file.write(error_line)


input_file_path = input("Введите путь к вашему файлу логов: ")
# можно для примера ввести путь до файла example_ERROR.txt

filter_errors(input_file_path)
