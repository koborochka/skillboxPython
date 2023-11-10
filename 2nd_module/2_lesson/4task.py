films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо",
         "Отступники", "Деревня"]
favoriteFilms = []

filmsCount = int(input("Сколько фильмов хотите добавить? "))

for film_number in range(filmsCount):
    favFilm = input("Введите название фильма: ")
    if favFilm in films:
        favoriteFilms.append(favFilm)
    else:
        print(f"Ошибка: фильма {favFilm} у нас нет :(")

print("Ваш список любимых фильмов: ",", ".join((str(item) for item in favoriteFilms)))
