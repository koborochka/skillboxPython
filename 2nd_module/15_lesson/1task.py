class File:
    def __init__(self, file_name, mode='r'):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_name, self.mode)
        except FileNotFoundError:
            print(f"File '{self.file_name}' not found. Creating a new file.")
            self.file = open(self.file_name, 'w+')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"An error occurred: {exc_type.__name__}: {exc_value}")


file_name = 'example.txt'

with File(file_name) as file:
    # Доступ к файлу и его использование
    file.write("Hello, World!")

# Контекст закрытия файла и обработка исключений осуществляется автоматически
