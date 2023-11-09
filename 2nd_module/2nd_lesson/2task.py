players = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]

firstDayCompParticitants = []
for playerId in range(0, len(players), 2):
    firstDayCompParticitants.append(players[playerId])

print(firstDayCompParticitants)