class App:
    def __init__(self):
        self.routes = {}

    def get(self, path):
        return self.routes.get(path)

    def callback(self, path):
        def decorator(func):
            self.routes[path] = func
            return func

        return decorator

# Создаем экземпляр приложения
app = App()

# Реализация декоратора callback
def callback(path):
    return app.callback(path)

# Пример использования
@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

# Основной код
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
