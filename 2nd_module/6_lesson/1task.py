violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
duration = 0

songs_count = int(input("Сколько песен выбрать? "))

for _ in range(songs_count):
    song = input("Название песни: ")
    if song in violator_songs:
        duration += violator_songs[song]
    else:
        print("Такой песни нет")

print("Общее время звучания песен: {:.2f} минут".format(duration))