def calculatePlaylistTime(selectedSongs):
    totalTime = sum(song[1] for song in selectedSongs)
    return totalTime

violatorSongs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

N = int(input("Сколько песен выбрать? "))

selectedSongs = []
for i in range(1, N + 1):
    songName = input(f"Название {i}-й песни: ")
    for song in violatorSongs:
        if songName.lower() == song[0].lower():
            selectedSongs.append(song)
            break
    else:
        print(f"Песни с названием '{songName}' не найдено в списке.")

totalTime = calculatePlaylistTime(selectedSongs)
print(f"Общее время звучания песен — {totalTime:.2f} минуты")
